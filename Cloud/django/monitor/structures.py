import json
import django
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import loader
from django import forms
from django.forms import formset_factory
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import CreateView

from sensor.models import *
from sensor.sensor import valid_sensor

from rest_framework import permissions, viewsets, status, views
from rest_framework.response import Response

from monitor.models import *
from monitor.rates import edit_rate

def index(request):
    template = loader.get_template('edit_structures.html')
    context = {}
    return HttpResponse(template.render(context, request))

class struct_lots(views.APIView):
    @csrf_exempt
    def get(self, request, format=None):
        lots = structures.objects.all()
        serialized = structures_serialized(lots, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    @csrf_exempt
    def post(self, request, format=None):
        old_lots = structures.objects.all()
        old_lots.delete()
        new_lots_raw = structures_serialized(data=json.loads(request.body), many=True)
        new_lots_raw.is_valid()
        
        new_lots = new_lots_raw.save()
        return Response({}, status=status.HTTP_200_OK)

class struct_sections(views.APIView):
    @csrf_exempt
    def get(self, request, format=None):
        all_secs = sections.objects.all()
        all_secs = sections_serialized(all_secs, many=True)
        return Response(all_secs.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        return Response({}, status=status.HTTP_200_OK)

class edit_structures(views.APIView):
    @csrf_exempt
    def get(self, request, format=None):
        lots = structures.objects.all()
        serialized = structures_serialized(lots, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    @csrf_exempt
    def post(self, request, format=None):
        old_methods = payment_method.objects.all()
        old_methods.delete()
        new_methods_raw = json.loads(request.body)
        new_methods_raw = payment_method_serialized(data=new_methods_raw, many=True)
        new_methods_raw.is_valid()
        new_methods = new_methods_raw.save()
        return Response({}, status=status.HTTP_200_OK)

