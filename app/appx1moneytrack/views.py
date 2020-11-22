#[VIEWS / appx1moneytrack]

from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .services import *
from .service_pdf import *

pruebas= "Este es un texto de pruebas"
category = (
('Comida'),
('Despensa'),
('Servicios'),
('Extras')
)

owner = (
('G'),
('D'),
)

type = (
('PRI'),
('PUB'),
)


def index_moneytrack_all(request):
	registroslist = Registrogasto.objects.filter(owner="G")
	datostotales = totalgastosAll() ### servicio distinto
	reporteurl = "/mon/reportall"
	return render(
		request,'index_moneytrack.html',
		{'registroslistx':registroslist, 'pruebasx':pruebas,
		'categoryx':category, 'datostotalesx':datostotales,
		'ownerx':owner, 'typex': type, 'reporteurlx':reporteurl}
	)

def index_moneytrack_pub(request):
	registroslist = Registrogasto.objects.filter(type = "PUB")
	datostotales = totalgastosPublic() ### servicio distinto
	reporteurl = "/mon/reportpub"
	return render(
		request,'index_moneytrack.html',
		{'registroslistx':registroslist, 'pruebasx':pruebas,
		'categoryx':category, 'datostotalesx':datostotales,
		'ownerx':owner, 'typex': type,'reporteurlx':reporteurl}
	)


#formoney para el nuevo registro del gasto
def save_formoney_reg(request):
	if request.method == 'POST':
		registro_cantidad = request.POST['newreg_quantity']
		registro_concepto = request.POST['newreg_concept']
		registro_categoria = request.POST['newreg_categoryselect']
		registro_owner = request.POST['newreg_ownerselect']
		registro_type = request.POST['newreg_typeselect']
		registrogasto = Registrogasto(
			quantity = registro_cantidad,
			concept = registro_concepto,
			category = registro_categoria,
			owner = registro_owner,
			type = registro_type
			)
		registrogasto.save()
		print("Nuevo registro agregado: " + registro_cantidad + "/" +  registro_concepto )
		return redirect ('index_moneytrack_pub')

def clear_form_reg(request,idx):
	reg = Registrogasto.objects.get(pk=idx)
	reg.delete()
	return redirect('index_moneytrack_pub')


def reportpub(request):
	type = "PUB"
	registros = Registrogasto.objects.filter(type = "PUB")
	datostotalesx = totalgastosPublic()
	response_import = report_fn(type,registros,datostotalesx)
	
	return response_import

def reportall(request):
	type = "GLI"
	registros = Registrogasto.objects.filter(owner="G")
	datostotalesx = totalgastosAll()
	response_import = report_fn(type,registros,datostotalesx)

	return response_import

