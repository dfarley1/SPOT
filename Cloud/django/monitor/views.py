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

from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.template import loader
import django
import sensor.models


def index(request):
    #stupid cookie thing we have to have.
    csrf_token = django.middleware.csrf.get_token(request)
    #which HTML file should we use?
    template = loader.get_template('monitor.html')
    
    #Do stuff here, fill a dictionary object from the database
    garage_status = spot_status.objects.all()
	
    #put that data into the HTML's context
    context = {'garage': garage_status}
    #render the HTML page
    return HttpResponse(template.render(context, request))

    