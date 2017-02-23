from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import Group, User, Permission
import uuid

from components import *


class SwishComponentActionPermissions(models.Model):

    name = models.CharField(max_length=75)

    component = models.CharField(max_length=75)
    action = models.CharField(max_length=75)

    attributes = models.CharField(max_length=75)

    profile_type = models.CharField(max_length=25, default='all')

    grant_action_at_activation = models.BooleanField(default=True)
    grant_action_at_registration = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Component Permissions'

    def __unicode__(self):
        return self.name


""""""
class SwishUserPermissions(models.Model):

    user = models.ForeignKey(User)
    attribute = models.CharField(max_length=75, blank=False)
    has_access = models.BooleanField(default=True)  # by default if its added it's available.

    #    access_given = models.DateTimeField()


    class Meta:
        verbose_name = 'User Permissions'

    def __unicode__(self):
        return str(self.user) + ' : ' + str(self.attribute)

