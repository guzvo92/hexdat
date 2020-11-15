from django.shortcuts import render


#[VIEWS / appmain0core]

from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
# Create your views here.

def index(request): return render(request,'index.html')

def pelasputo(request): return HttpResponse("Pelas puto tengo respaldos de la DB")
