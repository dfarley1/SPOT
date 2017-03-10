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

from django.db import models
from django.forms import ModelForm
import uuid

class spot_data(models.Model):
	uuid = models.UUIDField("UUID", primary_key = True, unique = True)
	#"static" metadata about spot
	active = models.BooleanField("Active", default=True)
	section = models.CharField("Section", max_length=20)
	number = models.IntegerField("Spot Number")
	description = models.CharField("Description", max_length=50)
	gpslat = models.FloatField("Latitude", null=True)
	gpslon = models.FloatField("Longitude", null=True)
	#"variable" current status
	last_update = models.DateTimeField("Last Update", auto_now=True)
	occ_status = models.SmallIntegerField("Occupied Status", default=0)
	occ_since = models.DateTimeField("Occupied Since")
	occ_license = models.CharField("Occupant License", max_length=20)
	
	def __str__(self):
		return (str(self.uuid))

class spot_data_form(ModelForm):
	class Meta:
		model = spot_data
		fields = ['active', 'section', 'number', 
				'description', 'gpslat', 'gpslon']




class spot_structs(models.Model):
	name = models.CharField("Structure", max_length=100)
	def __str__(self):
		return str(self.name)
	
class spot_structs_form(ModelForm):
	class Meta:
		model = spot_structs
		fields = ['name']




class spot_sections(models.Model):
	name = models.CharField("Section", max_length=100)
class spot_sections_form(ModelForm):
	class Meta:
		model = spot_sections
		fields = ['name']