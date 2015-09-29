from django.shortcuts import render, render_to_response
from django.template import RequestContext
from .models import CornerstoneUserProfile


def User(request):

     return render_to_response("base.html",
                          {'nodes':CornerstoneUserProfile.objects.all()},
                          context_instance=RequestContext(request))

