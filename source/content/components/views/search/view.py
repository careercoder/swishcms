from postings.models.postings import Posting

from ....library.alg import Index
import json

class PostingsSearch(object):

    def get(self, request=False):

        # get id
        path = request.path_info
        parts = path.split('/')

        try:
            # try:
            r = Index().get_results(request)

            pre_postings = json.dumps(r)
            postings = json.loads(pre_postings)
        except:
            postings = {}

        render = dict()
        render['view'] = 'postings/search/basic-search.html'   # app/component/view.html
        render['context'] = dict()
        render['context'] = {"postings": postings}

        return render





# Requestable Functions
def load_component(request):
    # action = request.page['overview'].action

    if not request.method == 'POST':
        response = PostingsSearch().get(request)
    else:
        pass
        # response = BoardDashboardAccountLogin().put(request)
    return response




"""


from jobsoft.jobsoft.api.postings.index import *
def postResults(request):
    ###############################################################
    # Swish Launch 1.0
    swish = SwishLoader().getPage(request)
    # return swish
    if not swish:
        return HttpResponse('You Do Not Have Access! Sorry.')


    active_jobboard = getActiveJobboard(request)

    r = Index().put_results(request, active_jobboard)

    return HttpResponse(r)


# Life Search
def searchResults2(request):


    ###############################################################
    # Swish Launch 1.0
    swish = SwishLoader().getPage(request)
    # return swish
    if not swish:
        return HttpResponse('You Do Not Have Access! Sorry.')


    active_jobboard = getActiveJobboard(request)

    try:
        # try:
        r = Index().get_results(request, swish['board'])

        #return HttpResponse(r)
        pre_postings = json.dumps(r)
        postings = json.loads(pre_postings)
    except:
        postings = {}


    #return  HttpResponse(postings['hits'][0]['title'])
    #active_jobboard.page.title = request.GET.get('q', False)


    context = {'jobboard': active_jobboard, 'postings': postings, 'swish':swish}
    template = 'jobs/search-results.html'

    #if active_jobboard.theme == 'swish':
    template = '_themes/swish/browse-jobs-2.swish.html'

    return render_to_response(template, context, context_instance=RequestContext(request))
    return HttpResponse("Search Results")



"""




