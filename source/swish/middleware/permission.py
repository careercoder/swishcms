from swish.models.swish.permissions import *

class PermissionMiddleware(object):

    def process_request(self, request):

        try:
            permissions = SwishUserPermissions.objects.filter(user=request.user)

            perm_list = []
            for permission in permissions:
                perm_list.append(permission.attribute)

            request.user.permissions = perm_list

        except:
            pass



