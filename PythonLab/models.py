from django.db import models
from django.conf import settings
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, UserManager)
from django.core import validators
from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _

import re


class Train(models.Model):
    name = models.CharField(max_length=128, default='Unknown')
    cityFrom = models.CharField(max_length=128, default='Unknown')
    cityTo = models.CharField(max_length=128, default='Unknown')
    cost = models.IntegerField(default=100)
    date = models.DateTimeField(null=True)


class Invoice(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    train = models.ForeignKey(Train)
    cost = models.IntegerField(default=100)
    paid = models.BooleanField(default=False)

"""
class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), max_length=30, unique=True,
        help_text=_('Required. 30 characters or fewer. Letters, numbers and '
                    '@/./+/-/_ characters'),
        validators=[
            validators.RegexValidator(re.compile('^[\w.@+-]+$'), _('Enter a valid username.'), 'invalid')
        ])
    full_name = models.CharField(_('full name'), max_length=254, blank=True)
    short_name = models.CharField(_('short name'), max_length=30, blank=True)
    email = models.EmailField(_('email address'), max_length=254, unique=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __unicode__(self):
        return self.username

    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.username)

    def get_full_name(self):
        full_name = self.full_name
        return full_name.strip()

    def get_short_name(self):
        return self.short_name.strip()
"""


