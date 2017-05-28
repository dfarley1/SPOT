from django.conf.urls import include, url
from django.contrib import admin
from rest_framework_nested import routers

from monitor.views import *
from monitor.structures import *

urlpatterns = [
    url(r'^create_lot/$', CreateLotView.as_view(), name='createLot'),
    url(r'^list_lots/$', ListLotView.as_view(), name='liststructures'),
    url(r'^edit_rate/$', EditRateView.as_view(), name='editRate'),
    url(r'^update_lots/$', EditRateView.as_view(), name='editRate'),
    url(r'^list_spots/$', ListSpotsView.as_view(), name='listSpots'),

    url(r'^payment_methods/$', payment_methods.as_view(), name='payment_methods'),
    url(r'^edit_structures/$', edit_structures.as_view(), name='edit_structures'),
    url(r'^struct_lots/$', struct_lots.as_view(), name='struct_lots'),
    url(r'struct_sections/$', struct_sections.as_view(), name='struct_sections'),
]