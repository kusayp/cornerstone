from django.conf.urls import url

from events import views

urlpatterns = [
	url(r'^event/', views.event, name='event'),
	url(r'^(?P<event_id>[0-9]+)/$', views.event_detail, name='event_detail'),
	url(r'^(?P<title>[\w-]+)/$', views.categories_detail, name='categories_detail'),
]