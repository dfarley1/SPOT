from django.conf.urls import url
import views

urlpatterns = [
	url(r'edit_info/', views.edit_info, name='edit_info'),
    url(r'^', views.index, name='monitor'),
]