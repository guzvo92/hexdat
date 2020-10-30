from django.shortcuts import render


#[VIEWS / appx1moneytrack]

from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
# Create your views here.

def index_moneytrack(request): return render(request,'index_moneytrack.html')
