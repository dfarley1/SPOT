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
import uuid

class spot_status(models.Model):
	sensor_uuid = models.UUIDField(
		primary_key = True,
		unique = True)
	last_update = models.DateTimeField(
		auto_now=True)
	occ_status = models.SmallIntegerField(
		default=0)
	occ_since = models.DateTimeField()
	occ_license = models.CharField(
		max_length=20)
	def __str__(self):
		return ("\n" + str(self.sensor_uuid) + 
			"\n\tlast_update: " + str(self.last_update) + 
			"\n\tocc_status: " + str(self.occ_status) + 
			"\n\tocc_license: " + self.occ_license + 
			"\n\tocc_since: " + str(self.occ_since) + "\n")
		
		
	

class spot_info(models.Model):
	sensor_uuid = models.UUIDField()
	section = models.CharField(max_length=20)
	number = models.IntegerField()
	description = models.CharField(max_length=50)
	def __str__(self):
		return ("\n" + str(self.sensor_uuid) +
			"\n\tsection: " + self.section +
			"\n\tnumber: " + self.number + 
			"\n\tsecription: " + self.description + "\n")
	
