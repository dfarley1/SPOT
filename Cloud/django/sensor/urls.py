from django.conf.urls import url

import sensor
import getUUID

urlpatterns = [
	url(r'getUUID/', getUUID.getUUID, name='getUUID'),
    url(r'^', sensor.sensor, name='sensor'),
]