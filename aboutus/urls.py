from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^wwb/', views.wwb, name='wwb'),
	url(r'^message/', views.message, name='message'),
	url(r'^leader/', views.leaders, name='leaders'),
	url(r'^registration/', views.registration, name='registration'),
	url(r'^(?P<slug>[\w-]+)/$', views.about, name='about'),
]