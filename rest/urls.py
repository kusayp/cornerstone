from django.conf import settings
from django.conf.urls import patterns, url, include
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
admin.autodiscover()

from rest_framework.routers import DefaultRouter

from hymn.view import *
from resources.view import *
from users.views import *


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'hymns', HymnViewSet)
router.register(r'stanzas', StanzaViewSet)
router.register(r'sermon', SermonViewSet)
router.register(r'sermon_categories', SermonCategoryViewSet)
router.register(r'devotion', DevotionViewSet)
router.register(r'register', RegisterViewSet)
router.register(r'comment', SermonCommentViewSet)
router.register(r'wwb', WwbViewSet)

urlpatterns = [
    url(r'^docs', include('rest_framework_swagger.urls')),
    url(r'^users/social-signup/', UserSocialSignUp.as_view()),
    url(r'^users/me/$', CurrentUserProfile.as_view()),
    url(r'^users/get-auth-token/$', obtain_auth_token, name='api-token'),

    url(r'^', include(router.urls)),
]
