from content.models.content import *
import json

class FormDesigner(object):

    def get(self, request=False):

        render = dict()
        render['view'] = 'builder/index.html'   # app/component/view.html
        render['context'] = {"test": "<h2>Hey baby</h2>"}

        return render




# Requestable Functions Allows Greater Control... Although I think it needs to be more 
# ellgant. 
def load_component(request):
    # action = request.page['overview'].action

    if not request.method == 'POST':
        response = FormDesigner().get(request)
    else:
        response = FormDesigner().get(request)
        # response = BoardDashboardAccountLogin().put(request)


    return response




