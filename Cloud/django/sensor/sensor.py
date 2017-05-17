from datetime import datetime
import django
import pytz
from django.http import HttpResponse, HttpResponseBadRequest
from django.template import loader

import monitor.logging
from models import spot_data

def sensor_main(request):
    csrf_token = django.middleware.csrf.get_token(request)
    if not valid_sensor(request):
        return HttpResponseBadRequest("Sensor UUID doesn't exist!")

    if request.method == 'GET':
        return sensor_GET(request)
    elif request.method == 'POST':
        return sensor_POST(request)
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])

#Returns the current database status of the specified sensor UUID
def sensor_GET(request):
    csrf_token = django.middleware.csrf.get_token(request)
    spot = spot_data.objects.get(uuid=request.GET['sensor_uuid'])
    response = HttpResponse("GET successful:\n" + str(spot))
    for field in spot._meta.fields:
        response[field.name] = str(getattr(spot, field.name))

    response.set_cookie('sensor_uuid', str(request.GET['sensor_uuid']))
    return response

#Updates the database status of the specified sensor UUID with contents of the POST arguments
def sensor_POST(request):
    csrf_token = django.middleware.csrf.get_token(request)
    #make sure everything is there
    if "occ_status" not in request.POST:
        return HttpResponseBadRequest("occ_status required")
    if "occ_since" not in request.POST:
        return HttpResponseBadRequest("occ_since required")
    if "occ_license" not in request.POST:
        return HttpResponseBadRequest("occ_license required")

    #what checks do we want to do on the data?
    if int(request.POST['occ_status']) > pow(2, 15):
        return HttpResponseBadRequest("occ_status illegal")
    #TODO: occ_since has no tz_info, need to convert
    #  POST['occ_since'] (string) -> datetime.datetime
    #  object and add tzinfo

    #get db entry
    spot = spot_data.objects.get(uuid=request.GET['sensor_uuid'])
    date_obj = datetime.strptime(request.POST["occ_since"], '%Y-%m-%d %H:%M:%S.%f')
    date_obj = pytz.utc.localize(date_obj)

    #a car has arrived at the spot
    if spot.occ_status == 0 and int(request.POST["occ_status"]) != 0:
        spot.occ_status = 2
        spot.occ_license = request.POST["occ_license"]
        monitor.logging.log_arrival(spot, date_obj)

    #a car has left the spot
    if spot.occ_status != 0 and int(request.POST["occ_status"]) == 0:
        spot.occ_status = 0
        spot.occ_license = ""
        spot.occupant = None
        monitor.logging.log_departure(spot, date_obj)

    #update with new values
    spot.occ_since = request.POST["occ_since"]
    spot.active = True

    #save the updated entry
    spot.save()

    return sensor_GET(request)

def valid_sensor(request):
    if "sensor_uuid" not in request.GET:
        return False
    uuid = request.GET['sensor_uuid']
    sensors = spot_data.objects.filter(uuid=uuid)
    if sensors.count() < 1:
        #print "sensor_uuid not in DB!"
        return False

    return True
    