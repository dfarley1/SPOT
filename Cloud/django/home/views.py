import pytz
import django
from django import forms
from django.forms import formset_factory
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import CreateView
from rest_framework import permissions, viewsets, status, views
from rest_framework.response import Response

from sensor.models import *
from monitor.models import *

def index(request):
    template = loader.get_template('mobile.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

#returns the user's currently occupied spot and event_log entry,
#  or most recent occupation spot and entry
def most_recent_event(user):
    return event_log.objects.filter(user=user).order_by('-start')[0]

class get_spot(views.APIView):
    @csrf_exempt
    def get(self, request, format=None):
        if request.user.is_anonymous:
            return Response({'message':'User not logged in'}, status=status.HTTP_401_UNAUTHORIZED)
        spot = most_recent_event(request.user).spot
        return Response(spot_data_serialized(spot).data, status=status.HTTP_200_OK)

class get_status(views.APIView):
    @csrf_exempt
    def get(self, request, format=None):
        if request.user.is_anonymous:
            return Response({'message':'User not logged in'}, status=status.HTTP_401_UNAUTHORIZED)
        event = most_recent_event(request.user)
        if event.end is None:
            #currently in spot
            currently_parked = 1
            total_charge = event.spot.section.get_total_charge(event.start)
            current_rate = event.spot.section.get_current_rate()
        else:
            #not in spot, use log
            currently_parked = 0
            total_charge = event.total_paid
            current_rate = 0 #does this matter?
        return Response({
            'currently_parked': currently_parked,
            'total_charge': total_charge,
            'current_rate': current_rate
        }, status=status.HTTP_200_OK)

class get_events(views.APIView):
    @csrf_exempt
    def get(self, request, format=None):
        events = event_log.objects.filter(user=request.user, end__isnull=False)
        return Response(event_log_serialized(events, many=True).data, status=status.HTTP_200_OK)
