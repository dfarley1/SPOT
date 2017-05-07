import views
import logging
from django.conf.urls import url

urlpatterns = [
    url(r'edit_info/', views.edit_info, name='edit_info'),
    url(r'view_structure/', views.view_structure, name='view_structure'),
    url(r'edit_structure/', views.edit_structure, name='edit_structures'),
    url(r'log_dump', logging.log_dump, name='log_dump'),
    url(r'^', views.index, name='monitor'),
]
