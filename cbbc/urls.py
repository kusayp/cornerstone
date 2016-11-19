"""Test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url 
from rest_framework import routers
from django.contrib import admin
from django.contrib.auth.views import password_reset_done, password_reset_confirm, password_reset_complete
from django.conf import settings
from django.views.generic import TemplateView
# from . import views

urlpatterns = [
	url(r'^', include('home.urls')), 
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^jet/dashboard', include('jet.dashboard.urls', 'jet-dashboard')),
    url(r'^admin/', admin.site.urls),
    url(r'^ministries/', include('ministries.urls')),
    url(r'^aboutus/', include('aboutus.urls')),
    url(r'^events/', include('events.urls')),
    url(r'^resources/', include('resources.urls')),
    url(r'^cont/', include('contact.urls')),
    url(r'^hymn/', include('hymn.urls')), 
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^api/v1.0/', include('rest.urls', namespace='api')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^resetpassword/passwordsent/$', password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', password_reset_complete, name='password_reset_complete'),
    url(r'^direct/$', TemplateView.as_view, {'template': 'direct.html','extra_context':{'showDirect':True}}),
]
