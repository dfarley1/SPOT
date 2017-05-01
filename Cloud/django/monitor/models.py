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
from django.db import models
from django.forms import ModelForm
from authentication.models import Account, AccountManager

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
            