#!/usr/bin/python 27
# Copyright 2013-2016
from django.http        import HttpResponse, HttpResponseRedirect
from django.shortcuts   import render_to_response
from django.template    import RequestContext
from django.conf        import settings     # Application Configuration
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django import template
from django.template import loader, Context

from ...library.api.menus.menus import *

from pydoc import locate


def initApp(request, requestedURI='/home/'):

    """
    :param request: scope of the user, request object
    :param requestedURI: the path being requested, from the URL.py
    :return: this returns the apprioriate response. it also allows us to skip many
             complicated task that would require us to add to each view, to where
             as we can start manipulation and data confirming withing this init of
             the application.
    """
    page = SwishMenu().get(request)
    #  page.elements = Swish().getPageElements(page.token)
    class_to_render = locate('board.views.get_request')
    render = class_to_render(request)

    return HttpResponse(render)




    template = 'launch/home.html'
    context = {}
    return render_to_response(template, context, context_instance=RequestContext(request))
