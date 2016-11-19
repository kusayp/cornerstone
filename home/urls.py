from django.conf.urls import url

from . import views
# from resources import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^(?P<pastor_id>[0-9]+)/$', views.pastor, name='pastor')
]