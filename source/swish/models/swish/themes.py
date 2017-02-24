from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import Group  # User, Group, Permission
import uuid


class SwishTheme(models.Model):

    token = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)

    name = models.CharField(max_length=75)
    description = models.TextField(blank=True)

    path = models.CharField(max_length=1064)
    slug = models.SlugField(max_length=1064, blank=True)

    params = models.TextField(blank=True)

    is_premium = models.BooleanField(default=False)

    class Meta:
        app_label = 'swish'
        verbose_name = 'Themes'

    def __unicode__(self):
        return self.name


class SwishThemeChildren(models.Model):

    token = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)

    parent = models.ForeignKey(SwishTheme)

    name = models.CharField(max_length=75)
    description = models.TextField(blank=True)

    path = models.CharField(max_length=1064)
    slug = models.SlugField(max_length=1064, blank=True)

    params = models.TextField(blank=True)

    is_premium = models.BooleanField(default=False)

    class Meta:
        app_label = 'swish'
        verbose_name = 'Theme > Children'

    def __unicode__(self):
        return self.name
