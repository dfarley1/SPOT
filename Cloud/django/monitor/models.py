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
import datetime
import pytz
from django.db import models
from django.forms import ModelForm
from rest_framework import serializers


from authentication.models import *
from sensor.models import *

class event_log(models.Model):
    start = models.DateTimeField("Arrival", null=True)
    end = models.DateTimeField("Departure", null=True)
    total_paid = models.FloatField("Total charge", default=0)
    spot = models.ForeignKey(spot_data, null=True)
    user = models.ForeignKey(Account, null=True)

    def __str__(self):
        string = "SPOT " + str(self.spot) + " occupied by "
        if self.user is None:
            string = string + str(self.spot.occ_license)
        else:
            string = string + str(self.user)
        string = string + (" from " + str(self.start) + " to " +
                           str(self.end) + " (" + str(self.dur_minutes()) + ") [$" +
                           str(self.total_paid) + "]")
        return string

    def dur_minutes(self):
        if self.start is None:
            return -2
        if self.end is None:
            end = pytz.utc.localize(datetime.datetime.now())
        else:
            end = self.end
        return int((end - self.start).total_seconds() / 60)

class event_log_serialized(serializers.ModelSerializer):
    spot = spot_data_serialized(read_only=True)
    class Meta:
        model = event_log
        depth = 3
        fields = ('start', 'end', 'total_paid', 'user', 'spot')

class payment_method(models.Model):
    name = models.CharField("Payment Method Name", max_length=100)
    purchase_price = models.FloatField("Purchase Price", default = 0.0)
    rate_modifier = models.FloatField("Rate Modifier", default = 1.0)


class payment_method_serialized(serializers.ModelSerializer):
    class Meta:
        model = payment_method
        depth = 2
        fields = ('id', 'name', 'purchase_price', 'rate_modifier')
    
    def create(self, validated_data):
        return payment_method.objects.create(**validated_data)
