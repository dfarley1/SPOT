from django.conf.urls import include, url
from django.contrib import admin
from rest_framework_nested import routers

from authentication.views import *

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^occupy/$', OccupyView.as_view(), name='occupy'),
]
