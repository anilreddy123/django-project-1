from django.shortcuts import render
from models import CornerstoneUserProfile

# Creating views

def cornerstone_profiles_list(request):

    # displaying user data on browser

    nodes = CornerstoneUserProfile.objects.all()
    return render(request, 'base.html', {'nodes' : nodes})