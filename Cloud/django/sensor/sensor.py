from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.template import loader
import django

def sensor(request):
    if request.method == 'GET':
        return sensor_GET(request)
    elif request.method == 'POST':
        return sensor_POST(request)
        
    return HttpResponseNotAllowed(['GET', 'POST'])

#Returns the current database status of the specified sensor UUID
def sensor_GET(request):
    print "--------- Sensor GET ----------"
    
    csrf_token = django.middleware.csrf.get_token(request)
    strParams = ''.join(str(e) for e in request.GET.items())
    
    return HttpResponse("GET requested successful:\n" + strParams)
    
    
#Updates the database status of the specified sensor UUID with contents of the POST arguments
def sensor_POST(request):
    print "-------- Sensor POST ----------"
    #for key, val in request.COOKIES:
    #    print(key, ' -> ', val)
    
    strParams = ''.join((str(e)+"\n") for e in request.POST.items())
    
    if not validSensor(request):
        return HttpResponseBadRequest("Invalid sensor")
        
    #if not request.POST.__contains__('')
    
    response = HttpResponse("Successful POST with:\n" + strParams)
    response['occ_valid'] = 1
    
    return response
    
def validSensor(request):
    if "sensor_uuid" not in request.GET:
        return False
    # if "sensor_id" not in DB already
    #   return False
    
    return True