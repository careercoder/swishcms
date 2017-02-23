from swish.models.swish.permissions import *
from employers.models.profile import *
from candidates.models.profile.main import *

# find a way to get this dynamically if more than one types of profiles can exist.
class ProfileMiddleware(object):

    def process_request(self, request):

        request.user.profile = dict()

        if request.user.is_authenticated():

            try:
                employer_profile = EmployerProfile.objects.get(user=request.user)
                request.user.profile['employer'] = employer_profile
            except EmployerProfile.DoesNotExist:
                request.user.profile['employer'] = False

            try:
                candidate_profile = CandidateProfile.objects.get(user=request.user)
                request.user.profile['candidate'] = candidate_profile
            except CandidateProfile.DoesNotExist:
                request.user.profile['candidate'] = False


            ## add other profile options.