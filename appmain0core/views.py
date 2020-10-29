from django.shortcuts import render


#[VIEWS / appmain1admin]

from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
# Create your views here.

def index(request): return render(request,'_index.html')
