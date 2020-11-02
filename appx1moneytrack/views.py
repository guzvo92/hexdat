#[VIEWS / appx1moneytrack]

from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .services import *


def index_moneytrack(request):
	registroslist = Registrogasto.objects.all()
	pruebas= "Este es un texto de pruebas"
	category = (
	('comida'),
	('despensa'),
	('pagos servicios'),
	('pagos extras')
	)
	
	datostotales = totalgastos()

	return render(
		request,'index_moneytrack.html',
		{'registroslistx':registroslist, 'pruebasx':pruebas, 'categoryx':category, 'datostotalesx':datostotales}
	)


#formoney para el nuevo registro del gasto
def save_formoney_reg(request):
	if request.method == 'POST':
		registro_cantidad = request.POST['newreg_quantity']
		registro_concepto = request.POST['newreg_concept']
		registro_categoria = request.POST['newreg_categoryselect']
		registrogasto = Registrogasto(
			quantity = registro_cantidad,
			concept = registro_concepto,
			category = registro_categoria,
			)
		registrogasto.save()
		print("Nuevo registro agregado: " + registro_cantidad + "/" +  registro_concepto )
		return redirect ('index_moneytrack')

def clear_form_reg(request,idx):
	reg = Registrogasto.objects.get(pk=idx)
	reg.delete()
	return redirect('index_moneytrack')
