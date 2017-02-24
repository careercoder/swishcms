class SwishMenu(object):

    from swish.models.swish.menus import SwishMenu

    def get(self, request):

        from swish.models.swish.menus import SwishMenu
        uri_alias = request.path_info
        menu = SwishMenu.objects.get(board=request.board, alias=uri_alias)

        return menu

