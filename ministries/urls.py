from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^men/', views.men, name='men'),
	url(r'^women/', views.women, name='women'),
	url(r'^youth/', views.youth, name='youth'),
	url(r'^children/', views.children, name='children'),
]