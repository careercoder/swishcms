from content.models.content import *
import json

class ContentArticle(object):

    def get(self, request=False):

        """
        :param request:
        :return:
        """
        # get id
        path = request.path_info
        parts = path.split('/')

        # get slug
        for part in parts:

            if part[:3] == 'id-':
                pid = part.split('-')[1]

        # return str(pid)
        try:
            page_params = json.loads(request.page.params)
            if 'content_id' in page_params:
                content = ContentPost.objects.get(token=page_params['content_id'])
        except:
            content = False


        render = dict()
        render['view'] = 'content/view_article.html'   # app/component/view.html
        render['context'] = {"content": content}

        return render




# Requestable Functions
def load_component(request):
    # action = request.page['overview'].action

    if not request.method == 'POST':
        response = ContentArticle().get(request)
    else:
        pass
        # response = BoardDashboardAccountLogin().put(request)


    return response




