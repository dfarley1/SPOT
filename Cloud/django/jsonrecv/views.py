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
import django

def index(request):
    if request.method == 'GET':
        print "--------- GET: Received ----------"
        print request.GET.lists()
        print "----------------------------------"
    #if request.method == 'POST':
    
    csrf_token = django.middleware.csrf.get_token(request)
    print "----------- Sending ------------\n"
    print "CSRF Token: " + csrf_token + "\n"
    print "---------------------------------\n\n"
    return HttpResponse("Hello, world. You're at the jsonrecv index.")

def sensor(request):
    if request.method == 'GET':
        #TODO: need more verification checks probably
        return sensorGET(request)
    elif request.method == 'POST':
        #TODO: definitely need more checks here
        return sensorPOST(request)
        
    return HttpResponse("Hello from sensor API")
    
    
def sensorGET(request):
    print "--------- Sensor GET ----------"
    
    strParams = ''.join(str(e) for e in request.GET.items())
    
    return HttpResponse("GET requested successful:\n" + strParams)
    
    

def sensorPOST(request):
    print "-------- Sensor POST ----------"
    
    strParams = ''.join(str(e) for e in request.GET.items())
    
    return HttpResponse("Someone made a POST request with \n" + strParams)
    
