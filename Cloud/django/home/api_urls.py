from django.conf.urls import include, url
from django.contrib import admin
from rest_framework_nested import routers

from home.views import *

urlpatterns = [
    url(r'^get_spot/$', get_spot.as_view(), name='get_spot'),
    url(r'^get_status/$', get_status.as_view(), name='get_status'),
    url(r'^get_events/$', get_events.as_view(), name='get_events'),
]