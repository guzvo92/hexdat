#[ VIEWS / appz1gman]
from django.shortcuts import render, HttpResponse, redirect
from .models import *

category = (
('Redes'),
('Automatizacion'),
('Desarrollo & Software'),
('Electronica & Raspberry')
)


def index_gman(request):
	projectlist1 = Registroproyecto.objects.all()
	db1 = Registroproyecto.objects.count()
	db2 = FinalRegistroproyecto.objects.count() 
	#se borra y cuenta desde 1 si hay diferencias #proyectos
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
	registro = Registroproyecto.objects.get(id=idx)
	registro.title = request.POST['newreg_title']
	registro.description = request.POST['newreg_description']
	registro.details = request.POST['newreg_details']
	registro.category = request.POST['newreg_categoryselect']
	registro.save()
	print("Proyecto editado: " + registro.title + "/" +  registro.category )
	return redirect ('admin_gman')


from django.views import View
from django.http import JsonResponse
from django.forms.models import model_to_dict

class ApiListView(View):
	def get(self, request):
		if('xtitle' in request.GET):
			#//Si el parametro ?title esta en el get tomalo y filtra ese valor
			GList = FinalRegistroproyecto.objects.filter(title__contains=request.GET['xtitle'])
		else:
			GList = FinalRegistroproyecto.objects.all()
			#//Se parsean los valores del queryset GList por casteo a una lista
		return JsonResponse(list(GList.values()), safe=False)

class ApiDetailView(View):
	def get(self, request, num):
		Gobject = FinalRegistroproyecto.objects.get(num=num)
		#//Se parsean los valores del queryset Gobject por diccionario
		Gobject_dict = model_to_dict(Gobject)
		
		#//agregamos este for porque al agregar una imagen en un diccionario
		#//me marca un error el JsonResponse diciendo que no puede serializar img
		#buscare cada item de imagen y lo hare string	
		for x in Gobject_dict:
			print()
			#//buscamos items con la palabra imagen
			if x.find("image") == 0: #lospositivos valen cero
				Val_Ser =  str(Gobject_dict[x]) #//obtener valor y parsealos a string
				Gobject_dict.update({x:Val_Ser}) #//Sustituyelo x valornvo

		#print(Gobject_dict)	
		return JsonResponse(Gobject_dict,safe=False)
		

from datetime import datetime, timedelta
tiemponow = (datetime.today()).strftime("[%Y-%m-%d] [%H.%M]")

def downloadapi(request):
	filename = "gmandb " + str(tiemponow)+ ".json"
	GList = FinalRegistroproyecto.objects.all()
	content = JsonResponse(list(GList.values()), safe=False)
	response = HttpResponse(content, content_type='text/plain') #//Render
	
   #// Esto me descarga el txt se edita el header Content-disposition
	response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
	return response

from django.shortcuts import render
from .forms import UploadDocumentForm

def uploadapi(request):
	formG = UploadDocumentForm()
	if request.method == 'POST':
		form = UploadDocumentForm(request.POST, request.FILES)  
		if form.is_valid():
			form.save()

	#renderiza pero si te llega un post de aqui haz lo del IF
	return render(request, 'upload_gman.html', locals())
