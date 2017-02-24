from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from pydoc import locate
from django.shortcuts import render

from swish.apps import *
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

import json

class SwishApplication(object):


    def run(self, request):

        #try:
            Application = dict()  # Start new application

            Application['swish'] = dict()
            Application['swish']['version'] = '0.5.1'
            Application['swish']['license'] = 'Private'
            Application['component'] = locate(str(request.page.component.path)+str(request.page.action.path) + '.load_component')(request)
            Application['elements'] = dict()
            Application['template'] = SwishConfig().settings()['default_template']
            # Default template, or custom detection run. -- should this be done here?
            # Template Overriding from View
            try:
                if Application['component']['templateoverride']:
                    Application['template'] = Application['component']['view']
                    # Default template, or custom detection run. -- should this be done here?
            except:
                pass

            try:
                Application['context'] = {"component": Application["component"],}
                # add the component view
                Application['context'].update(Application['component']['context'])
                # add the component context
            except:
                pass 
                
            # detect the response type we need.
            try:
                Application['type'] = Application["component"]["type"]
            except:
                Application['type'] = 'component'

            t = loader.get_template(Application["template"])
            c = Application['context']

            # handle response types
            if Application['type'] == 'json':
                return HttpResponse(json.dumps(Application['component']['context']))

            return HttpResponse(t.render(c, request)) # , content_type='application/xhtml+xml')


        #except:
        #    return HttpResponse("(Something went wrong)")

@csrf_exempt
def start(request, params={}):

    return SwishApplication().run(request)


