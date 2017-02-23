from swish.models.pages.main import *
from swish.models.swish.menus import SwishMenu


class PageMiddleware(object):
    def process_request(self, request):
        '''
            Remember :: /component/action/(optional)params/
            -- the first check is to see if a database over ride has been applied.
        '''

        params = dict()
        params['uri_path'] = request.path_info
        params['uri_parts'] = params['uri_path'].split('/')


        if params['uri_path'] == '' or params['uri_path'] == '/' or not params['uri_path']:
            try:
                request.page = SwishMenu.objects.get(home=True)
            except SwishMenu.DoesNotExist:
                request.page = False

        else:
            try:
                request.page = SwishMenu.objects.get(alias=params['uri_path'])

            except SwishMenu.DoesNotExist:
                # At this point if it hits this area - we know no page has been found let/s search deeper.
                try:
                    request.page = SwishMenu.objects.get(alias='/' + str(params['uri_parts'][1]) + '/'  + str(params['uri_parts'][2]) + '/')
                except:
                    try:
                        request.page = SwishMenu.objects.get(alias='/' + str(params['uri_parts'][1]) + '/')
                    except SwishMenu.DoesNotExist:
                        request.page = False

        # Populating Meta Data. Should this be done here or somewhere else, since this is "PAGE"?
        if request.page:
            request.page.meta = dict()
            request.page.meta['title'] = request.page.title  # default set by menu title.
