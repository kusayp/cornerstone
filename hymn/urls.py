from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.hymn, name='hymn'),
	url(r'^(?P<hymn_id>[0-9]+)/$', views.stanza_detail, name='stanza_detail'),
]

