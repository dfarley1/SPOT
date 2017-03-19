from django.shortcuts import render
from django import forms
from django.forms import formset_factory
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import loader
import django
from sensor.models import *

# Create your views here.

def index(request):
	if 'sensor_uuid' in request.GET:
		uuid=request.GET['sensor_uuid']
		spot = spot_data.objects.get(uuid=uuid)
	else:
		uuid=""
	
	
	
	if 'user_auth' in request.GET:
		user=request.GET['user_auth']
	else:
		user=""
	
	return HttpResponse("uuid: " + uuid + "<br>" + 
		"section: "+spot.section+"<br>"+
		"number: "+str(spot.number)+"<br>"+
		"user: " + user)
