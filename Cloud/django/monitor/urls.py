import views
import logging
import structures
from django.conf.urls import url

urlpatterns = [
    url(r'payment_methods', views.payment_methods_view, name='payment_methods'),
    url(r'edit_structures', structures.index, name='edit_structures'),
    url(r'log_dump', logging.log_dump, name='log_dump'),
    url(r'^', views.index, name='monitor'),
]
