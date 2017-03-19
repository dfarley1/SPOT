from django.conf.urls import url
import views

urlpatterns = [
	url(r'edit_info/', views.edit_info, name='edit_info'),
	url(r'list_structures/', views.list_structures, name='list_structures'),
	url(r'view_structure/', views.view_structure, name='view_structure'),
	url(r'edit_structure/', views.edit_structure, name='edit_structures'),
    url(r'hub/', views.hub, name='hub'),
	url(r'^', views.index, name='monitor'),
]
