from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.template import loader
import django
from models import spot_status, spot_info

def sensor_main(request):
	csrf_token = django.middleware.csrf.get_token(request)
	if not valid_sensor(request):
		return HttpResponseBadRequest("Sensor UUID doesn't exist!  Use getUUID to obtain one.")

	if request.method == 'GET':
		return sensor_GET(request)
	elif request.method == 'POST':
		return sensor_POST(request)
	else:
		return HttpResponseNotAllowed(['GET', 'POST'])

#Returns the current database status of the specified sensor UUID
def sensor_GET(request):
	csrf_token = django.middleware.csrf.get_token(request)
	print "--------- Sensor GET ----------"
	
	spot = spot_status.objects.get(sensor_uuid=request.GET['sensor_uuid'])
	
	response = HttpResponse("GET successful:\n" + str(spot))
	for field in spot._meta.get_fields():
		response[field.name] = str(getattr(spot, field.name))
	
	return response
	
	
#Updates the database status of the specified sensor UUID with contents of the POST arguments
def sensor_POST(request):
	print "-------- Sensor POST ----------"
	
	strParams = ''.join((str(e)+"\n") for e in request.POST.items())
	
	response = HttpResponse("Successful POST with:\n" + strParams)
	response['occ_valid'] = 1
	
	return response
	
def valid_sensor(request):
	if "sensor_uuid" not in request.GET:
		return False
	uuid = request.GET['sensor_uuid']
	q = spot_status.objects.filter(sensor_uuid=uuid)
	if q.count() < 1:
		#print "sensor_uuid not in DB!"
		return False
	
	return True
	