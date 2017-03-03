from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.template import loader
from django.utils import timezone
import django
import datetime
import models
import uuid

def getUUID(request):
	if request.method == 'GET':
		return getUUID_GET(request)
	else:
		return HttpResponseNotAllowed(['GET'])

def getUUID_GET(request):
	if 'mac_addr' in request.GET:
		mac_addr = request.GET['mac_addr']
	else:
		return HttpResponseBadRequest("MAC address required!")
	new_uuid = uuid.uuid1(long(mac_addr))
	
	new_info = models.spot_info(
		sensor_uuid=new_uuid,
		number=0)
	new_info.save()
	new_status = models.spot_status(
		sensor_uuid=new_uuid,
		occ_status=0,
		occ_since=datetime.datetime.min.replace(tzinfo=timezone.utc))
	new_status.save()
	
	response = HttpResponse(str(new_uuid))
	csrf_token = django.middleware.csrf.get_token(request)
	response['sensor_uuid'] = new_uuid
	response.set_cookie('sensor_uuid', str(new_uuid))
	
	return response