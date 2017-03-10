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

from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import loader
import django
from sensor.models import *
from sensor.sensor import valid_sensor
from django import forms
from django.forms import formset_factory


def index(request):
	#stupid cookie thing we have to have.
	csrf_token = django.middleware.csrf.get_token(request)
	#which HTML file should we use?
	template = loader.get_template('monitor.html')
	
	#Do stuff here, fill a dictionary object from the database
	garage_data = spot_data.objects.all()
	
	#put that data into the HTML's context
	context = {
		'garage_data': garage_data}
	#render the HTML page
	return HttpResponse(template.render(context, request))

	
def edit_info(request):
	spot = spot_data.objects.get(uuid=request.GET['sensor_uuid'])
	if not valid_sensor(request):
		return HttpResponseBadRequest("Sensor UUID doesn't exist!")
		
	if request.method == 'POST':
		form = spot_data_form(request.POST, instance=spot)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/monitor/')
		else:
			return HttpResponseRedirect('/not_valid/')
		
	else:
		form = spot_data_form(instance=spot)
	return render(
		request, 
		'edit_info.html', 
		{'form':form, 'sensor_uuid': request.GET['sensor_uuid'],}
	)


def view_structure(request):
	csrf_token = django.middleware.csrf.get_token(request)
	garage_data = spot_data.objects.all()
	
	return render(request, 'view_structure.html', {'garage': garage_data})


def list_structures(request):
	csrf_token = django.middleware.csrf.get_token(request)
	structures = spot_structs.objects.all()
	
	return render(request, 'list_structures.html', {'structures': structures})


def edit_structure(request):
	if 'name' in request.GET:
		structure = spot_structs.objects.get(name=request.GET['name'])
		print "using existing structure" + str(structure)
	else:
		structure = spot_structs()
		print "using new structure" + str(structure)
	
	if request.method == "POST":
		form = spot_structs_form(request.POST, instance=structure)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/monitor/list_structures/')
		else:
			return HttpResponseRedirect('/not_valid/')
	else:
		form = spot_structs_form(instance=structure)
	return render(
		request, 
		'edit_structure.html', 
		{'form':form, 'name':request.GET['name']})