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
from authentication.models import Account, AccountManager
from sensor.models import spot_data

class parking_rates(models.Model):
    start_time = models.TimeField("Start time")
    end_time = models.TimeField("End time")
    days = models.IntegerField("Days", default=0)
    section = models.CharField("Section(s)", max_length=20)
    spot = models.IntegerField("SPOT(s)")
    rate = models.IntegerField("Rate per hour")

    def contains(self, time):
        if time > self.start_time and time < self.end_time:
            day_of_week = 2**time.weekday()
            if self.days & day_of_week is True:
                return True
        return False

class event_log(models.Model):
    start = models.DateTimeField("Arrival", null=True)
    end = models.DateTimeField("Departure", null=True)
    spot = models.ForeignKey(spot_data, null=True, related_name="spot_occupied")
    user = models.ForeignKey(Account, null=True, related_name="occupant")

    def __str__(self):
        string = "SPOT " + str(self.spot) + " occupied by "
        if self.user is None:
            string = string + str(self.spot.occ_license)
        else:
            string = string + str(self.user)
        string = string + (" from " + str(self.start) + " to " +
                           str(self.end) + " (" + str(self.dur_minutes()) + ")")

    def dur_minutes(self):
        if self.start is None:
            return -2
        if self.end is None:
            end = pytz.utc.localize(datetime.datetime.now())
        else:
            end = self.end
        return int((end - self.start).total_seconds() / 60)
