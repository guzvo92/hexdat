#[ VIEWS / appz1gman]
from django.shortcuts import render, HttpResponse, redirect
from .models import *

category = (
('Redes'),
('Automatizacion'),
('Desarrollo & Software'),
('Electronica & Raspberry')
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

#eval = rowevaluate() #paso array con conteos de renglon YA NO SE USO

def index_gman(request):
	projectlist1 = Registroproyecto.objects.all()
	db1 = Registroproyecto.objects.count()
	db2 = FinalRegistroproyecto.objects.count()
	conteo = 1

	if db1 != db2:
		print("[GMAN] -> Diferencia de DBs detectada")
		FinalRegistroproyecto.objects.all().delete()

		for x in projectlist1:
			if conteo > 1:
				prevx = conteo - 1
			else: prevx = 1

			if conteo == db1:
				nextx = conteo
			else: nextx = conteo + 1
			XFinalRegistroproyecto = FinalRegistroproyecto(
				num = conteo,
				next = nextx,
				prev = prevx,
				title = x.title,
				description = x.description,
				details = x.details,
				category = x.category,
				image1 = x.image1,
				image2 = x.image2,
				image3 = x.image3,
				image4 = x.image4,
				image5 = x.image5,
				)
			XFinalRegistroproyecto.save()
			print(str(XFinalRegistroproyecto.num) + " / " + str(XFinalRegistroproyecto))
			conteo += 1
	else: print("[GMAN] -> No hay diferencias de DBs")

	projectlist2 = FinalRegistroproyecto.objects.all()
	return render(
		request,'index_gman.html',
		{'projectlistx':projectlist2,'conteox':conteo}
	)


def getproject(request,idx):
	#recordar que num no es el pk la db que uso es la recorrida
    project = FinalRegistroproyecto.objects.get(num=idx)
    return render(
		request,'get_Project_gman.html',
		{'projectx':project,}
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
	registro = FinalRegistroproyecto.objects.get(num=idx)
	registro.title = request.POST['newreg_title']
	registro.description = request.POST['newreg_description']
	registro.details = request.POST['newreg_details']
	registro.category = request.POST['newreg_categoryselect']
	registro.save()
	print("Proyecto editado: " + registro.title + "/" +  registro.category )
	return redirect ('admin_gman')
