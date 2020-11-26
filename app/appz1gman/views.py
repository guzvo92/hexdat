#[ VIEWS / appz1gman]
from django.shortcuts import render, HttpResponse, redirect
from .models import *

category = (
('Electronica'),
('Redes'),
('Automatizacion'),
('Desarrollo web')
)

def index_gman(request):
	projectlist = Registroproyecto.objects.all
	#tot_proy = len(projectlist)
	#print(tot_proy)
	print(projectlist)
	return render(
		request,'index_gman.html',
		{'projectlistx':projectlist,}
	)

def admin_gman(request):
    projectlist = Registroproyecto.objects.all
    return render(
		request,'admin_gman.html',
		{'projectlistx':projectlist,'categoryx':category}
	)

#formoney para el nuevo registro del gasto
def save_project(request):
	if request.method == 'POST':
		registro_title = request.POST['newreg_title']
		registro_description = request.POST['newreg_description']
		registro_category = request.POST['newreg_categoryselect']


		registroproyecto = Registroproyecto(
			title = registro_title,
			description = registro_description,
			category = registro_category,
			)
		registroproyecto.save()
		print("Nuevo proyecto agregado: " + registro_title + "/" +  registro_category )
		return redirect ('admin_gman')

def clear_project(request,idx):
	reg = Registroproyecto.objects.get(pk=idx)
	reg.delete()
	return redirect('admin_gman')

def edit_project(request,idx):
	reg = Registroproyecto.objects.get(pk=idx)

	return render(
		request,'edit_gman.html',
		{'xproject':reg,'categoryx':category}
	)

def save_edit_project(request,idx):
	if request.method == 'POST':
		reg = Registroproyecto.objects.get(pk=idx)
		registro_title = request.POST['newreg_title']
		registro_description = request.POST['newreg_description']
		registro_category = request.POST['newreg_categoryselect']


		registroproyecto = Registroproyecto(
			id = idx,
			title = registro_title,
			description = registro_description,
			category = registro_category,

			)
		registroproyecto.save()
		print("Nuevo proyecto agregado: " + registro_title + "/" +  registro_category )
		return redirect ('admin_gman')

''' Ejemplo que crea objeto sin fecha por el array
def save_edit_project(request,idx):
	if request.method == 'POST':
		reg = Registroproyecto.objects.get(pk=idx)
		registro_title = request.POST['newreg_title']
		registro_description = request.POST['newreg_description']
		registro_category = request.POST['newreg_categoryselect']


		registroproyecto = Registroproyecto(
			id = idx,
			title = registro_title,
			description = registro_description,
			category = registro_category,

			)
		registroproyecto.save()
		print("Nuevo proyecto agregado: " + registro_title + "/" +  registro_category )
		return redirect ('admin_gman')
'''

def save_edit_project(request,idx):

		registro = Registroproyecto.objects.get(pk=idx)
		registro.title = request.POST['newreg_title']
		registro.description = request.POST['newreg_description']
		registro.category = request.POST['newreg_categoryselect']

		registro.save()
		print("Proyecto editado: " + registro.title + "/" +  registro.category )
		return redirect ('admin_gman')
