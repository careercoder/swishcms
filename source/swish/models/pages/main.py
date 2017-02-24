from __future__ import unicode_literals
from django.db import models

import uuid

from ..swish.themes import *


from ..swish.modules import SwishElements

SwishPageStatusChoices = ((0, "Disabled"),
                          (1, "Enabled"),
                          (2, "Under Review"),
                          (3, "Pending"),
                          (4, "Not Approved"))



class SwishPageAttribute(models.Model):

    token = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    page = models.ForeignKey('swish.SwishPage')
    name = models.CharField(max_length=35)
    value = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name + ' ' + self.board.title



class SwishPage(models.Model):

    token = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)

    title = models.CharField(max_length=150)
    slug = models.CharField(max_length=1064)
    path = models.CharField(max_length=1064)

    theme = models.ForeignKey(SwishTheme, blank=True, null=True)
    template = models.CharField(max_length=75, default="content.html")

    meta_title = models.CharField(max_length=255, blank=False)
    meta_description = models.CharField(max_length=255, blank=True)
    meta_keywords = models.CharField(max_length=255, blank=True)

    content = models.TextField(blank=True)
    content_override_main = models.BooleanField(default=False)

    elements = models.ManyToManyField(SwishElements, blank=True)  # Positions on the Page
    attributes = models.ManyToManyField(SwishPageAttribute, blank=True, null=True)

    status = models.IntegerField(default=1, choices=SwishPageStatusChoices)

    params = models.TextField(blank=True)

    def __unicode__(self):
        return self.title


class SwishSettings(models.Model):

    token = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    theme = models.ForeignKey(SwishTheme)

    def __unicode__(self):
        return self.token


