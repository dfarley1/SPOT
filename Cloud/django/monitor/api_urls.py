from django.conf.urls import include, url
from django.contrib import admin
from rest_framework_nested import routers

from monitor.views import *

urlpatterns = [
    url(r'^create_lot/$', CreateLotView.as_view(), name='createLot'),
    url(r'^list_lots/$', ListLotView.as_view(), name='liststructures'),
    url(r'^edit_rate/$', EditRateView.as_view(), name='editRate'),
    url(r'^update_lots/$', EditRateView.as_view(), name='editRate'),
    url(r'^list_spots/$', ListSpotsView.as_view(), name='listSpots'),

    url(r'^payment_methods/$', payment_methods.as_view(), name='payment_methods')
]