# Copyright 2015 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import uuid
import pickle
import datetime
from django.db import models
from django.forms import ModelForm
from rest_framework import serializers

from authentication.models import Account, AccountManager
from authentication.serializers import AccountSerializer

class structures(models.Model):
    name = models.CharField("Structure", max_length=100)
    def __str__(self):
        return str(self.name)

class structures_serialized(serializers.ModelSerializer):
    class Meta:
        model = structures
        fields = ('name',)

def rates_default():
    return [[0 for i in xrange(96)] for j in xrange(7)]

class sections(models.Model):
    name = models.CharField("Section", max_length=100)
    structure = models.ForeignKey(structures, null=True)
    rates = models.TextField("Rates Array", default=rates_default)

    #saves a 7x96 2D rate array.  7 days in week, 96 15-minute chunks in day
    def rates_save(self, rates):
        # Check dimensions
        if len(rates) is 7:
            for i in range(0, 6):
                if len(rates[i]) is not 96:
                    return False
            self.rates = pickle.dumps(rates)
            rates.save()
            return True

    def rates_load(self):
        return pickle.loads(self.rates)

    def time_to_index(self, time):
        return time.hour * 4 + int(time.minute/15)

    def minute_of(self, index):
        return index * 15

    #get current rate
    def get_current_rate(self, curr_time):
        dow = curr_time.date.weekday()
        tod = self.time_to_index(curr_time.time)
        ret = self.rates[dow][tod]
        return ret

    def get_total_charge(self, start_time, end_time):
        rates = self.rates_load()
        for x in range(len(rates)):
            for y in range(len(rates[x])):
                rates[x][y] = 1
        self.save()

        if start_time.date.weekday() == end_time.date.weekday():
            total_charge = 0
            for i in range(self.time_to_index(start_time.time), self.time_to_index(end_time.time)):
                chunk_start = self.minute_of(i)
                parked_start = start_time.time.hour * 60 + start_time.time.minute
                chunk_end = self.minute_of(i+1)
                parked_end = end_time.time.hour * 60 + end_time.time.minute
                interval_start = max(chunk_start, parked_start)
                interval_end = min(chunk_end, parked_end)
                total_charge += (((interval_end - interval_start)/15) *
                                (rates[start_time.date.weekday()][i]/4))
            return total_charge
        else:
            return -1

    def __str__(self):
        return str(self.name + " (" + self.structure.name + ")")

class sections_serialized(serializers.ModelSerializer):
    class Meta:
        model = sections
        fields = ('name','structure')


class spot_data(models.Model):
    uuid = models.UUIDField("UUID", primary_key=True, unique=True)
    #"static" metadata about spot
    active = models.BooleanField("Active", default=True)
    section = models.ForeignKey(sections, null=True)
    number = models.IntegerField("Spot Number")
    description = models.CharField("Description", max_length=50)
    gpslat = models.FloatField("Latitude", null=True)
    gpslon = models.FloatField("Longitude", null=True)
    rate = models.FloatField("OLD RATE", default=0)
    #"variable" current status
    last_update = models.DateTimeField("Last Update", auto_now=True)
    occ_status = models.SmallIntegerField("Occupied Status", default=0)
    occ_since = models.DateTimeField("Occupied Since")
    occ_license = models.CharField("Occupant License", max_length=20)
    occupant = models.ForeignKey(Account, null=True)


    def __str__(self):
        return str(self.uuid)

    def pretty_str(self):
        if self.section != None:
            str_structure = self.section.structure
        else:
            str_structure = "None"
        return str_structure + " " + str(self.section) + ", " + str(self.number)


class spot_data_serialized(serializers.ModelSerializer):
    class Meta:
        model = spot_data
        depth = 2

        fields = ('uuid', 'active', 'section', 'number',
                  'description', 'gpslat', 'gpslon',
                  'rate', 'last_update', 'occ_status',
                  'occ_since', 'occ_license', 'occupant')
