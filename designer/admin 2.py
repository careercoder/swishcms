from django.contrib import admin

# Register your models here.
from models.content import *

admin.site.register(ContentPost)
admin.site.register(ContentCategory)

