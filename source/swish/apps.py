from __future__ import unicode_literals

from django.apps import AppConfig


class SwishConfig(object):

    def settings(self):

        swish = dict()
        swish['name']   = 'swish'
        swish['default_template'] = 'themes/critter/base.html'   # path set param to default template you desire.


        return swish