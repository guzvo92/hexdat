#[ VIEWS / appz1gman]
from django.shortcuts import render, HttpResponse, redirect
from .models import *

category = (
('Electronica'),
('Redes'),
('Automatizacion'),
('Desarrollo web')
)

#Escencialmemte es para evaluar el # de caract de cada item de registroproyecto
# los divide x renglon de 4 items
def rowevaluate():
	conteo = 1
	arraylens = []
	total = Registroproyecto.objects.count()

	R1 = []
	R2 = []
	R3 = []
	R4 = []

	for x in Registroproyecto.objects.all():
		querycount = len(x.description)
		divisor = conteo/4

		if divisor <= 1:
			R1.append(querycount)
		if divisor > 1 and divisor <= 2:
			R2.append(querycount)
		if divisor > 2 and divisor <= 3:
			R3.append(querycount)
		if divisor > 3 and divisor <= 4:
			R4.append(querycount)
		conteo += 1

	espaciado=130 #porque #caract /= height adecuado
	try: maxr1 = max(R1) + espaciado
	except: maxr1 = 0
	try: maxr2 = max(R2) + espaciado
	except: maxr2 = 0
	try: maxr3 = max(R3) + espaciado
	except: maxr3 = 0
	try: maxr4 = max(R4) + espaciado
	except: maxr4 = 0

	print("[R1]" + str(R1) + " [MAX] = "+ str(maxr1))
	print("[R2]" + str(R2) + " [MAX] = "+ str(maxr2))
	print("[R3]" + str(R3) + " [MAX] = "+ str(maxr3))
	print("[R4]" + str(R4) + " [MAX] = "+ str(maxr4))

	maxarray = [ maxr1, maxr2, maxr3, maxr4]

	return maxarray


def index_gman(request):
	projectlist = Registroproyecto.objects.all
	eval = rowevaluate() #paso array con conteos
	conteo = 0

	return render(
		request,'index_gman.html',
		{'projectlistx':projectlist,'evalx':eval,'conteox':conteo}
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
		registro_details = request.POST['newreg_details']
		registro_category = request.POST['newreg_categoryselect']


		registroproyecto = Registroproyecto(
			title = registro_title,
			description = registro_description,
			details = registro_details,
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
	registro = Registroproyecto.objects.get(pk=idx)
	registro.title = request.POST['newreg_title']
	registro.description = request.POST['newreg_description']
	registro.details = request.POST['newreg_details']
	registro.category = request.POST['newreg_categoryselect']
	registro.save()
	print("Proyecto editado: " + registro.title + "/" +  registro.category )
	return redirect ('admin_gman')


def getproject(request,idx):
    project = Registroproyecto.objects.get(pk=idx)
    return render(
		request,'view_Project_gman.html',
		{'projectx':project,}
	)
