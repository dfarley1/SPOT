# Copyright 2015 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#	 http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
from monitor.serializers import *
from monitor.rates import edit_rate


def index(request):
	#stupid cookie thing we have to have.
	csrf_token = django.middleware.csrf.get_token(request)
	#which HTML file should we use?
	template = loader.get_template('monitor.html')

	#Do stuff here, fill a dictionary object from the database
	garage_data = spot_data.objects.all()
	lot_directory = structures.objects.all()

	#put that data into the HTML's context
	context = {'garage_data': garage_data,
               'spot_data': garage_data,
               'lot_directory': lot_directory}
	#render the HTML page
	return HttpResponse(template.render(context, request))

def payment_methods_view(request):
    template = loader.get_template('payment_methods.html')
    context = {}
    return HttpResponse(template.render(context, request))

def edit_rates_view(request):
    template = loader.get_template('edit_rates.html')
    context = {}
    return HttpResponse(template.render(context, request))

class CreateLotView(views.APIView):
    @csrf_exempt
    def post(self, request, format=None):
        data = json.loads(request.body)
        old_info = data.get('old_info', None)
        new_info = data.get('new_info', None)

        #if there's no new_info then what are we even doing here?
        if new_info is None:
            return Response({
                'message': 'Missing new_info'
            }, status=status.HTTP_400_BAD_REQUEST)

        #if there's no old info then we're trying to add a new entry
        #else we're updating an existing entry
        if old_info is None:
            #check for existing structure
            old_struct = structures.objects.filter(name=new_info)
            #if the structure exists, don't create a duplicate
            #else create a new instance and save it
            if len(old_struct) > 0:
                return Response({
                    'message': 'Name already exists, no change'
                }, status=status.HTTP_202_ACCEPTED)
            else:
                new_struct = structures(name=new_info)
                new_struct.save()
                return Response({
                    'message': 'Structure created'
                }, status=status.HTTP_201_CREATED)
        else:
            #check for existing structures
            old_struct = structures.objects.filter(name=old_info)
            num_structs = len(old_struct)
            #if there's none existing with that name, return error
            #elif there's one existing entry, update it
            #else we dun fuck'd up
            if num_structs == 0:
                return Response({
                    'message': 'No structure with that name found'
                }, status=status.HTTP_400_BAD_REQUEST)
            elif num_structs == 1:
                struct = old_struct[0]
                old_name = struct.name
                struct.name = new_info
                return Response({
                    'message': ('Strucutre \'' + old_name + '\' renamed to ' + new_info + '\'.')
                }, status=status.HTTP_200_OK)
            else:
                #this should never happen
                return Response({
                    'message': 'Something has gone VERY wrong'
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @csrf_exempt
    def old_post(self, request, format=None):
        # Load data into model
        data = json.loads(request.body)
        lot_name = data.get('lot_name', None)

        # Save attributes to new Lot and store in DB
        newLot = structures()
        newLot.name = lot_name
        newLot.save()

        if lot_name is None:
            return Response({
                'status': 'Unauthorized',
                'message': 'Empty Name'
            }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            print "[SERVER]: Succesfully processed \'" + lot_name + "\'"
            return Response({
                'status': 'Success',
                'message': 'New lot processed!'
            }, status=status.HTTP_200_OK)

class ListLotView(views.APIView):
    @csrf_exempt
    def get(self, request, format=None):
        # Load entire structure table, and serialize every Lot instance
        lot_directory = structures.objects.all()
        serialized = LotSerializer(lot_directory, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

class ListSpotsView(views.APIView):
    @csrf_exempt
    def get(self, request, format=None):
        # Load entire structure table, and serialize every Spot instance
        spots_directory = spot_data.objects.all()
        serialized = SpotSerializer(spots_directory, many=True)
        print('[SERVER]: Returning Spots Directory!')
        return Response(serialized.data, status=status.HTTP_200_OK)

class EditRateView(views.APIView):
    @csrf_exempt
    def post(self, request, format=None):
      # Load data from Form
      data = json.loads(request.body)
      spot_number = data.get('spot_number', None)
      spot_rate   = data.get('spot_rate', None)

      # Upate spot attributes
      edit_rate(spot_number, spot_rate)

      return Response({
          'status': 'Success',
          'message': 'Spot rate changed'
      }, status=status.HTTP_200_OK)

class EditLotView(views.APIView):
    @csrf_exempt
    def get(self, request, format=None):
        # Load entire structure table, and serialize every Spot instance
        spots_directory = spot_data.objects.all()
        serialized = SpotSerializer(spots_directory, many=True)
        print('[SERVER]: Returning Spots Directory!')
        return Response(serialized.data, status=status.HTTP_200_OK)

class struct_sections(views.APIView):
    @csrf_exempt
    def get(self, request, format=None):
        secs = sections.objects.all()
        serialized = sections_serialized(secs, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

class payment_methods(views.APIView):
    @csrf_exempt
    def get(self, request, format=None):
        payment_methods = payment_method.objects.all()
        serialized = payment_method_serialized(payment_methods, many=True)
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

class edit_rates(views.APIView):
    @csrf_exempt
    def get(self, request, format=None):
        lots = structures.objects.filter(name=request.GET['lot'])[0]
        ssection = sections.objects.filter(name=request.GET['section'], structure=lots)
        section = ssection[0]
        rates = section.rates_load()

        return Response(rates, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        msg = json.loads(request.body)
        lot_str = msg['lot']
        sec_str = msg['section']
        new_rates = msg['rates']

        lot = structures.objects.filter(name=lot_str)[0]
        section = sections.objects.filter(name=sec_str, structure=lot)[0]
        
        section.rates_save(new_rates)

        return Response({}, status=status.HTTP_200_OK)
