from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^sermon/', views.sermon, name='sermon'),
	url(r'^(?P<sermon_id>[0-9]+)/$', views.sermon_detail, name='sermon_detail'),
	url(r'^devotion/', views.devotion, name='devotion'),
	# url(r'^devot/$', views.devot, name='devot'),
	url(r'^(?P<name>[\w-]+)/$', views.category_detail, name='category_detail'),
]