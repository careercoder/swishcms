from __future__ import unicode_literals
from django.db import models

from swish.models.swish.permissions import *


class Application(models.Model):

    title = models.CharField(max_length=75)
    description = models.TextField(blank=True)
    author = models.CharField(max_length=75, blank=True)
    installed_version = models.CharField(max_length=25, default='0.0.1')

    application_path = models.CharField(max_length=1064, blank=True)

    updated_at = models.DateTimeField(auto_now=True)