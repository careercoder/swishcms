from __future__ import unicode_literals

from django.apps import AppConfig


class AppConfig():

    def settings(self):

        app = dict()
        app['name'] = 'Form Designer'
        app['description'] = ''
        app['version'] = '1.0'
        app['component'] = 'designer'
        app['alias'] = '/designer/'
        app['path'] = 'designer.components'
        app['author'] = 'Jody Fitzpatrick'

        #################################################
        '''
           The Idea of Views.
        '''
        #
        app['views'] = [
            {
                "name": "Editor",
                "default_alias": "/designer/editor/",
                "path": ".views.designer.home",
                "description": "View article",
                "permissions": [],
            },
        ]

        return app



def install():
    return AppConfig().settings()
