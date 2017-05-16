import django
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.forms import formset_factory
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader

from sensor.models import *

def edit_rate(number, rate):
  spot = spot_data.objects.get(number=number)
  spot.rate = rate
  print(spot.rate)
  spot.save()


  #spot.section.rate = rate
  
 #active__isnull=, section__isnull=,
 #                                 number__isnull=, description__isnull=, 
 #                                  gpslat__isnull=, gpslon__isnull=,
  #spot.save()
