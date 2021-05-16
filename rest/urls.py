from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from rest_framework import permissions
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from hymn.view import *
from resources.view import *
from users.views import *

admin.autodiscover()
schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

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
    url(r'^docs', schema_view),
    url(r'^users/social-signup/', UserSocialSignUp.as_view()),
    url(r'^users/me/$', CurrentUserProfile.as_view()),
    url(r'^users/get-auth-token/$', obtain_auth_token, name='api-token'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    url(r'^', include(router.urls)),
]
