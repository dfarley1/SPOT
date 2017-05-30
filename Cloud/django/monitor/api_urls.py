from django.conf.urls import include, url
from django.contrib import admin
from rest_framework_nested import routers

from monitor.views import *
from monitor.structures import *

urlpatterns = [
    #lots
    url(r'^create_lot/$', CreateLotView.as_view(), name='createLot'),
    url(r'^list_lots/$', ListLotView.as_view(), name='liststructures'),
    url(r'^update_lots/$', EditRateView.as_view(), name='editRate'),
    url(r'^edit_structures/$', edit_structures.as_view(), name='edit_structures'),
    #sections
    url(r'^list_sections/$', struct_sections.as_view(), name='struct_sections'),
    url(r'^edit_rates/$', edit_rates.as_view(), name='edit_rates'),
    #spots
    url(r'^list_spots/$', ListSpotsView.as_view(), name='listSpots'),
    #payments
    url(r'^payment_methods/$', payment_methods.as_view(), name='payment_methods'),

]
