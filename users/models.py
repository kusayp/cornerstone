from django.db import models
from django.conf import settings
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
import os
# from PIL import Image
from django.core.files.storage import default_storage as storage
from rest_framework.authtoken.models import Token

from datetime import datetime


class PCUserManager(BaseUserManager):

    def create_user(self, email, first_name, last_name, password=None):
        """
        Creates and saves a User with the given email,
        first_name, last_name and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, first_name, last_name):
        """
        Creates and saves a superuser with the given email, password,
        first_name and last_name.
        """
        user = self.create_user(email,
                                password=password,
                                first_name=first_name,
                                last_name=last_name)
        user.is_admin = True
        user.save(using=self._db)
        return user


class PCUser(AbstractBaseUser):
    TODAY = datetime.now()

    TODAY_PATH = TODAY.strftime("%Y/%m/%d/%H:%M:%S")

    USER_DIR = 'NEW_CACHES/AVATARS/' + TODAY_PATH + '/'

    email = models.EmailField(
        verbose_name=_('email address'),
        max_length=255,
        unique=True,
    )
    username = models.CharField(
        verbose_name=_('username'),
        max_length=100,
        default='self'
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100, null=True, blank=True )
    church = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    is_pastor = models.BooleanField(default=False)

    objects = PCUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']


    def get_full_name(self):
        return self.first_name+' '+self.last_name

    def get_short_name(self):
        return self.first_name


    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    def __str__(self):
        return self.email

    class Meta:
        ordering = ('id', 'first_name',)
        verbose_name = _('user')
        verbose_name_plural = _('users')


@receiver(post_save, sender=PCUser)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)