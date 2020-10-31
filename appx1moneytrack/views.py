from django.shortcuts import render


#[VIEWS / appx1moneytrack]

from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect

from .models import Registrogasto
# Create your views here.

def index_moneytrack(request):
    registroslist = Registrogasto.objects.all()
    return render(request,'index_moneytrack.html',
    {'registroslistx':registroslist})


#formoney para el nuevo registro del gasto
def save_formoney_reg(request):
    if request.method == 'POST':
        registro_cantidad = request.POST['newreg_quantity']
        registro_concepto = request.POST['newreg_concept']
        registrogasto = Registrogasto(
			quantity = registro_cantidad,
            concept = registro_concepto,
			)
        registrogasto.save()
        print("Nuevo registro agregado: " + registro_cantidad + "/" +  registro_concepto )
        return redirect ('index_moneytrack')

def clear_form_reg(request,idx):
	reg = Registrogasto.objects.get(pk=id)
	reg.delete()
	return redirect('index_moneytrack')
