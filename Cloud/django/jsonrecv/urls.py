from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.sensor, name='sensor'),
]