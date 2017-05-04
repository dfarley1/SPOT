import django
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.forms import formset_factory
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader

from monitor.models import event_log
from sensor.models import spot_data
from sensor.sensor import valid_sensor

def log_arrival(sensor, start_time):
    #start a log event at the given spot
    events = event_log.objects.filter(spot=sensor, start__isnull=False, end__isnull=True)
    events = events.order_by('-start')
    if len(events) > 0:
        event = events[0]
        event.start = min(event.start, start_time)
    else:
        event = event_log(spot=sensor, start=start_time, end=None, user=None)
    event.save()

def log_occupancy(sensor, user):
    #occupy a spot with a user after beacon transmission
    events = event_log.objects.filter(spo=sensor).order_by('-start')
    if len(events) > 0:
        event = events[0]
        event.user = user
        event.save()

def log_departure(sensor, end_time):
    #end a log event when user leaves
    events = event_log.objects.filter(spot=sensor, start__isnull=False)
    events = events.order_by('-start')
    if len(events) > 0:
        event = events[0]
        if event.end is None:
            event.end = end_time
        else:
            event.end = max(event.end, end_time)
        event.save()

def log_dump(request):
    events = event_log.objects.all()

    template = loader.get_template('log_dump.html')
    context = {'log_data': events}
    return HttpResponse(template.render(context, request))
