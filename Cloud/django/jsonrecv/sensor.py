from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.template import loader
import django

def sensorGET(request):
    print "--------- Sensor GET ----------"
    
    csrf_token = django.middleware.csrf.get_token(request)
    strParams = ''.join(str(e) for e in request.GET.items())
    
    return HttpResponse("GET requested successful:\n" + strParams)
    
    

def sensorPOST(request):
    print "-------- Sensor POST ----------"
    #for key, val in request.COOKIES:
    #    print(key, ' -> ', val)
    
    strParams = ''.join((str(e)+"\n") for e in request.POST.items())
    
    response = HttpResponse("Successful POST with:\n" + strParams)
    response['occ_valid'] = 1
    
    return response
    

    
def validSensor(request):
    if "sensor_id" not in request.GET:
        return False
    # if "sensor_id" not in DB already
    #   return False
    
    return True