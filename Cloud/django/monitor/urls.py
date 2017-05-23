import views
import logging
from django.conf.urls import url

urlpatterns = [
    url(r'payment_methods', views.payment_methods_view, name='payment_methods'),
    url(r'log_dump', logging.log_dump, name='log_dump'),
    url(r'^', views.index, name='monitor'),
]
