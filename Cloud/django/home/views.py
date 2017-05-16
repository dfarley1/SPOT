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


class get_spot(views.APIView):
    @csrf_exempt
    def get(self, request, format=None):
        if request.user.is_anonymous:
            return Response({
                'message':'User not logged in'
            }, status=status.HTTP_401_UNAUTHORIZED)
        spot_in = spot_data.objects.filter(occupant=request.user)
        if len(spot_in) == 0:
            #get the last spot they were in
            print 0
        else:
            #return this spot
            spot_in = spot_in[0]
        return Response(spot_data_serialized(spot_in).data, status=status.HTTP_200_OK)

class get_status(views.APIView):
    @csrf_exempt
    def get(self, request, format=None):
        if request.user.is_anonymous:
            return Response({
                'message':'User not logged in'
            }, status=status.HTTP_401_UNAUTHORIZED)
        spot_in = spot_data.objects.filter(occupant=request.user)
        total_charge = 0
        current_rate = 0
        if len(spot_in) == 0:
            #get last spot
            total_charge = 1
        else:
            spot_in = spot_in[0]
            total_charge = spot_in.section.get_total_charge()
        return Response({
            'total_charge': total_charge,
            'current_rate': current_rate
        }, status=status.HTTP_200_OK)

class get_events(views.APIView):
    @csrf_exempt
    def get(self, request, format=None):
        events = event_log.objects.all()
        return Response(event_log_serialized(events, many=True).data, status=status.HTTP_200_OK)
