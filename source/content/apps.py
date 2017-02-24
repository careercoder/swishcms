from __future__ import unicode_literals

from django.apps import AppConfig


class ContentConfig():

    def settings(self):

        app = dict()
        app['name'] = 'Blog'
        app['description'] = ''
        app['version'] = '1.0'
        app['component'] = 'content'
        app['alias'] = '/content/'
        app['path'] = 'content.components'
        app['author'] = 'Jody Fitzpatrick'

        #################################################
        '''
           The Idea of Views.
        '''
        #
        app['views'] = [
            {
                "name": "View Article",
                "default_alias": "/content/view/",
                "path": ".views.single.view",
                "description": "View article",
                "permissions": [],
            },
        ]

        return app



def install():
    return ContentConfig().settings()
