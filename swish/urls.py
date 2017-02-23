from django.conf.urls import url
from django.contrib import admin

from swish.application.start import start
from django.conf.urls import include, url

urlpatterns = [
    
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', start),
    url(r'^(?P<params>.+)/', start),
]
