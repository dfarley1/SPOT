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

from django.conf.urls import include, url
from django.contrib import admin
from rest_framework_nested import routers

from authentication.views import AccountViewSet
from mysite.views import *

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)

urlpatterns = [
    #templates
    url(r'^sensor/', include('sensor.urls')),
    url(r'^monitor/', include('monitor.urls')),
    #url(r'^payment_methods/', include('monitor.urls')),
    url(r'^user/', include('user.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #api
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/auth/', include('authentication.api_urls')),
    url(r'^api/v1/monitor/', include('monitor.api_urls')),
    url(r'^api/v1/user/', include('user.api_urls')),
    #catch-all
    url('^.*$', IndexView.as_view(), name='index'),
]
