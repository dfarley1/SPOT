import views
import logging
from django.conf.urls import url

urlpatterns = [
    url(r'log_dump', logging.log_dump, name='log_dump'),
    url(r'^', views.index, name='monitor'),
]
