from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import Group  # User, Group, Permission

import uuid

swish_menu_type_choices = (('component', 'Component'), ('url', 'URL'), ('alias', 'Alias'), ('separator', 'Separator'))


class SwishElements(models.Model):

    token = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=True)
    
    title = models.CharField(max_length=75)
    note = models.CharField(max_length=255, blank=True)

    content = models.TextField(blank=True)

    ordering = models.IntegerField(default=0)
    position = models.CharField(max_length=50)

    is_published = models.BooleanField(default=False)

    access = models.ManyToManyField(Group, blank=True)  # if no access free for all.

    showtitle = models.BooleanField(default=False)
    params = models.TextField(blank=True)

    template = models.CharField(max_length=255, blank=True, null=True)
    element_path = models.CharField(max_length=255, blank=True, null=True)

    type = models.CharField(max_length=30, blank=True)

    published = models.DateTimeField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField()


    class Meta:
        verbose_name = 'Module'
        verbose_name_plural = 'Modules'

    def __unicode__(self):
        return self.title


# swish/elements/menu/render-menu.html
"""

class SwishElement(models.Model):

    token = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)

    board = models.ForeignKey(Board)

    # theme = models.ForeignKey(SwishTheme)

    title = models.CharField(max_length=75, blank=True)
    show_title = models.BooleanField(default=False)

    content = models.TextField(blank=True)

    position = models.CharField(max_length=50, blank=True)

    params = models.TextField(blank=True)

    def __unicode__(self):
        return str(self.id) + ' ' + str(self.title)


CREATE TABLE IF NOT EXISTS `#__modules` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `asset_id` int(10) unsigned NOT NULL DEFAULT 0 COMMENT 'FK to the #__assets table.',
  `title` varchar(100) NOT NULL DEFAULT '',
  `note` varchar(255) NOT NULL DEFAULT '',
  `content` text NOT NULL,
  `ordering` int(11) NOT NULL DEFAULT 0,
  `position` varchar(50) NOT NULL DEFAULT '',
  `checked_out` int(10) unsigned NOT NULL DEFAULT 0,
  `checked_out_time` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `publish_up` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `publish_down` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `published` tinyint(1) NOT NULL DEFAULT 0,
  `module` varchar(50) DEFAULT NULL,
  `access` int(10) unsigned NOT NULL DEFAULT 0,
  `showtitle` tinyint(3) unsigned NOT NULL DEFAULT 1,
  `params` text NOT NULL,
  `client_id` tinyint(4) NOT NULL DEFAULT 0,
  `language` char(7) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `published` (`published`,`access`),
  KEY `newsfeeds` (`module`,`published`),
  KEY `idx_language` (`language`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 DEFAULT COLLATE=utf8mb4_unicode_ci AUTO_INCREMENT=87;
"""