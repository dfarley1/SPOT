from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.template import loader
import django

def getUUID(request):
    if request.method == 'GET':
        return getUUID_GET(request)
    elif request.method == 'POST':
        return getUUID_POST(request)
        
    return HttpResponseNotAllowed(['GET'])

def getUUID_GET(request):
	return HttpResponse("not yet")
	
def getUUID_POST(request):
	return HttpResponse("not yet")