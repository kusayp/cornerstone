from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^contact/', views.contact, name='contact'),
	url(r'^404/', views.handler404, name='handler404'),
]