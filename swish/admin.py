from django.contrib import admin

from models.pages.main import *

from models.swish.menus import *
from models.swish.modules import  *
from models.swish.permissions import *

from models.swish.components import *

class SwishPageAdmin(admin.ModelAdmin):
    list_display  = ('id', 'board', 'title')
    # list_filter = (('board',))
    search_fields = ['id', 'title', 'path', ]


class SwishComponentActionsMenu(admin.ModelAdmin):
    list_display = ('name', 'component', 'path', )


class SwishMenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'alias', )


admin.site.register(SwishMenu, SwishMenuAdmin)
admin.site.register(SwishMenuTypes)
admin.site.register(SwishElements)
admin.site.register(SwishSettings)
admin.site.register(SwishTheme)
admin.site.register(SwishThemeChildren)
admin.site.register(SwishUserPermissions)
admin.site.register(SwishComponent)
admin.site.register(SwishComponentActionPermissions)
admin.site.register(SwishComponentActions, SwishComponentActionsMenu)

# admin.site.register(SwishPageAttribute)
# admin.site.register(SwishPage, SwishPageAdmin)
