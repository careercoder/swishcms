from swish.models.swish.menus import *

class BoardDashboardAccountLogin(object):

    def get(self, request=False):

        menu = SwishMenu.objects.filter(board=request.board)

        render = dict()
        render['template'] = 'swish/elements/menu/side-menu.html'   # app/component/view.html
        render['data'] = {"menu": menu}

        return render



# Requestable Functions
def load_element(request):
    # action = request.page['overview'].action

    if not request.method == 'POST':
        response = BoardDashboardAccountLogin().get(request)
    else:
        response = BoardDashboardAccountLogin().put(request)


    return response
