from .models import *

def totalgastos():
    registros = Registrogasto.objects.all()
    total_comida = 0
    total_despensa = 0
    total_servicios = 0
    total_extras = 0


    #filtros https://docs.djangoproject.com/en/3.1/topics/db/queries/
    Query_comida = Registrogasto.objects.filter(category="comida")
    Query_despensa = Registrogasto.objects.filter(category="despensa")
    Query_servicios = Registrogasto.objects.filter(category="pagos servicios")
    Query_extras = Registrogasto.objects.filter(category="pagos extras")
    
    for query in Query_comida:
      total_comida += query.quantity
    
    for query in Query_despensa:
      total_despensa += query.quantity
 
    for query in Query_servicios:
      total_servicios += query.quantity

    for query in Query_extras:
      total_extras += query.quantity

    dic_datostotales = {
        'total_comida' : total_comida, 
        'total_despensa' : total_despensa,
        'total_servicios' : total_servicios,
        'total_extras' :total_extras
        }

    return dic_datostotales



