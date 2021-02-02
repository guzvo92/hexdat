#views.py [appz0projects]

from django.shortcuts import render

from .segmentados.makers import *

CreaUrlsAppz0projects("app/appz0projects/segmentados/urls.py")

def index(request): return render(request,'profilerender.html')