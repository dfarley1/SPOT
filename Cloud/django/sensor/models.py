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
import pytz
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
            self.save()
            return True

    def rates_load(self):
        return pickle.loads(self.rates)

    def get_current_rate(self, time=pytz.utc.localize(datetime.datetime.now())):
        rates = self.rates_load()
        return rates[time.date().weekday()][time.hour * 4 + int(time.minute/15)]

    def get_total_charge(self, start_time, end_time=pytz.utc.localize(datetime.datetime.now())):
        rates = self.rates_load()
        mask = rates_default()
        #get start and end indices [day, chunk]
        start_n = [start_time.date().weekday(), start_time.hour * 4 + int(start_time.minute/15)]
        end_n = [end_time.date().weekday(), end_time.hour * 4 + int(end_time.minute/15)]
        #fill everything in between start_n and end_n with 1
        i = start_n[0]
        while i <= end_n[0]:
            for j in range(96):
                if i == start_n[0]: j = max(start_n[1], j)
                if i == end_n[0]: j = min(end_n[1], j)
                mask[i][j] = 1
            i = (i+1)%7
        #fix partial for start chunk
        start_int = start_time.minute
        end_int = 15 * (int(start_int / 15) + 1)
        mask[start_n[0]][start_n[1]] = (end_int - start_int) / 15.0
        #fix partial for end chunk
        end_int = end_time.minute
        start_int = 15 * int(end_int/15)
        mask[end_n[0]][end_n[1]] = (end_int - start_int)/15.0

        #apply mask to rates
        total_charge = 0
        for i in range(7):
            for j in range(96):
                total_charge += rates[i][j]/4.0 * mask[i][j]
        print mask
        print total_charge
        return total_charge


    def __str__(self):
        return str(self.name + " (" + self.structure.name + ")")

class sections_serialized(serializers.ModelSerializer):
    class Meta:
        model = sections
        fields = ('name', 'structure')


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
        return str(str_structure) + " " + str(self.section) + ", " + str(self.number)


class spot_data_serialized(serializers.ModelSerializer):
    class Meta:
        model = spot_data
        depth = 2

        fields = ('uuid', 'active', 'section', 'number',
                  'description', 'gpslat', 'gpslon',
                  'rate', 'last_update', 'occ_status',
                  'occ_since', 'occ_license', 'occupant')
