from django.conf.urls import url

import sensor
import getUUID

urlpatterns = [
	url(r'getUUID/', getUUID.getUUID, name='getUUID'),
	url(r'getuuid/', getUUID.getUUID, name='getuuid'),
	url(r'^', sensor.sensor_main, name='sensor'),
]