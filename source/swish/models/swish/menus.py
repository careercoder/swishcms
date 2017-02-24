from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import Group  # User, Group, Permission

from themes import SwishTheme
from modules import SwishElements
from components import SwishComponent, SwishComponentActions

import uuid

swish_menu_type_choices = (('component', 'Component'), ('url', 'URL'), ('alias', 'Alias'), ('separator', 'Separator'))


class SwishMenuTypes(models.Model):

    token = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=True)
    name = models.CharField(max_length=75)
    slug = models.SlugField(max_length=75)  # asset id
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Menu Type'
        verbose_name_plural = 'Menu Types'

    def __unicode__(self):
        return self.name


class SwishMenu(models.Model):

    token = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    
    menutype = models.ForeignKey(SwishMenuTypes, blank=True, null=True)

    title = models.CharField(max_length=255)
    alias = models.CharField(max_length=400)
    note = models.CharField(max_length=255, blank=True)

    meta_title = models.CharField(max_length=155, blank=True)
    meta_description = models.CharField(max_length=155, blank=True)
    meta_keywords = models.CharField(max_length=155, blank=True)

    link = models.CharField(max_length=1024, blank=True)
    type = models.CharField(max_length=25, choices=swish_menu_type_choices)

    component = models.ForeignKey(SwishComponent)  # CharField(max_length=250)  # employer.account.create
    action = models.ForeignKey(SwishComponentActions)  # the action of z component
    """ Notes """
    # Path to Component ( I eventuall want univeral - auto detect )
    # ex.) employer.account.create ( swish will know how to handle )
    theme = models.ForeignKey(SwishTheme, blank=True, null=True)

    elements = models.ManyToManyField(SwishElements, blank=True)

    params = models.TextField(blank=True, default="{}")
    home = models.BooleanField(default=False)

    access = models.ManyToManyField(Group, blank=True)  # if no access free for all.

    published = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'


    def __unicode__(self):
        return self.title


"""

CREATE TABLE IF NOT EXISTS `#__menu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `menutype` varchar(24) NOT NULL COMMENT 'The type of menu this item belongs to. FK to #__menu_types.menutype',
  `title` varchar(255) NOT NULL COMMENT 'The display title of the menu item.',
  `alias` varchar(400) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL COMMENT 'The SEF alias of the menu item.',
  `note` varchar(255) NOT NULL DEFAULT '',
  `path` varchar(1024) NOT NULL COMMENT 'The computed path of the menu item based on the alias field.',
  `link` varchar(1024) NOT NULL COMMENT 'The actually link the menu item refers to.',
  `type` varchar(16) NOT NULL COMMENT 'The type of link: Component, URL, Alias, Separator',
  `published` tinyint(4) NOT NULL DEFAULT 0 COMMENT 'The published state of the menu link.',
  `parent_id` int(10) unsigned NOT NULL DEFAULT 1 COMMENT 'The parent menu item in the menu tree.',
  `level` int(10) unsigned NOT NULL DEFAULT 0 COMMENT 'The relative level in the tree.',
  `component_id` int(10) unsigned NOT NULL DEFAULT 0 COMMENT 'FK to #__extensions.id',
  `checked_out` int(10) unsigned NOT NULL DEFAULT 0 COMMENT 'FK to #__users.id',
  `checked_out_time` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' COMMENT 'The time the menu item was checked out.',
  `browserNav` tinyint(4) NOT NULL DEFAULT 0 COMMENT 'The click behaviour of the link.',
  `access` int(10) unsigned NOT NULL DEFAULT 0 COMMENT 'The access level required to view the menu item.',
  `img` varchar(255) NOT NULL COMMENT 'The image of the menu item.',
  `template_style_id` int(10) unsigned NOT NULL DEFAULT 0,
  `params` text NOT NULL COMMENT 'JSON encoded data for the menu item.',
  `lft` int(11) NOT NULL DEFAULT 0 COMMENT 'Nested set lft.',
  `rgt` int(11) NOT NULL DEFAULT 0 COMMENT 'Nested set rgt.',
  `home` tinyint(3) unsigned NOT NULL DEFAULT 0 COMMENT 'Indicates if this menu item is the home or default page.',
  `language` char(7) NOT NULL DEFAULT '',
  `client_id` tinyint(4) NOT NULL DEFAULT 0,
"""

