from __future__ import unicode_literals
from django.db import models

from swish.models.swish.permissions import *

class SwishComponent(models.Model):


    name = models.CharField(max_length=75)
    component = models.CharField(max_length=75)  # the name of the component ( eg.) slug etc. )
    version = models.CharField(blank=True, max_length=11)  # eg.) 1.25.1291 version 1 . sub version 25 build 1291
    alias = models.CharField(max_length=75)        # the default loading path eg.) /job/ ## etc.
    description = models.TextField(blank=True)

    path = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Component'

    def __unicode__(self):
        return  self.name


class SwishComponentActions(models.Model):

    component = models.ForeignKey(SwishComponent)

    name = models.CharField(max_length=75)
    alias = models.CharField(max_length=75)
    type = models.CharField(max_length=75, default='view')
    description = models.TextField(blank=True)

    # permissions = models.ManyToManyField(SwishComponentActionPermissions)

    path = models.CharField(max_length=255)  ## appendable to the action only - must follow conventions.

    class Meta:
       verbose_name = 'Component Action'

    def __unicode__(self):
        return  self.name
