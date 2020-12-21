#[ VIEWS / appmain1admin]
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .forms import *

from django.contrib.auth import authenticate,login,logout


def no(request):
	return HttpResponse("esto es una prueba")


def register_page(request):
	registerformx = RegisterForm()

	if request.method == 'POST':
		register_form = RegisterForm(request.POST)
		if register_form.is_valid():
			register_form.save()
			return redirect ('register')

	return render (request, 'register.html',
			{'registerformg': registerformx})




def login_page(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request,user)
			return redirect ('profile' )

	return render (request, 'login.html')



def profile_page(request):

	if request.method == 'POST':
		registro_title = request.POST.get('title')
		registronota = Nota(
			title = registro_title,
			)
		registronota.save()




	return render (request, 'profile.html')
