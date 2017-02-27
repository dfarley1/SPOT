from django.conf.urls import url

from . import views
from . import monitor

urlpatterns = [
    url(r'^sensor/', views.sensor, name='sensor'),
    url(r'^monitor/', monitor.index, name='monitor')
]