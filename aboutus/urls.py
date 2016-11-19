from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^wwb/', views.wwb, name='wwb'),
	# url(r'^(?P<hymn_id>[0-9]+)/$', views.wwb_detail, name='wwb_detail'),
	url(r'^message/', views.message, name='message'),
	url(r'^(?P<slug>[\w-]+)/$', views.about, name='about'),
]