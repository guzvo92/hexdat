
#En los servicios estan todas las funciones no procesadas en views
from .models import *

def totalgastosPublic():
    
    xtotal_comida = 0
    xtotal_despensa = 0
    xtotal_servicios = 0
    xtotal_extras = 0


    #filtros https://docs.djangoproject.com/en/3.1/topics/db/queries/
    Query_comida = Registrogasto.objects.filter(category="Comida", type ="PUB")
    Query_despensa = Registrogasto.objects.filter(category="Despensa" , type ="PUB")
    Query_servicios = Registrogasto.objects.filter(category="Servicios" , type ="PUB")
    Query_extras = Registrogasto.objects.filter(category="Extras" , type ="PUB")

    for query in Query_comida:
      xtotal_comida += query.quantity

    for query in Query_despensa:
      xtotal_despensa += query.quantity

    for query in Query_servicios:
      xtotal_servicios += query.quantity

    for query in Query_extras:
      xtotal_extras += query.quantity

    xtotal_neto = xtotal_comida + xtotal_despensa + xtotal_servicios + xtotal_extras

    dic_datostotales = {
        'total_comida' : xtotal_comida,
        'total_despensa' : xtotal_despensa,
        'total_servicios' : xtotal_servicios,
        'total_extras' : xtotal_extras,
        'total_neto': xtotal_neto
        }

    return dic_datostotales

def totalgastosAll():

    xtotal_comida = 0
    xtotal_despensa = 0
    xtotal_servicios = 0
    xtotal_extras = 0


    #filtros https://docs.djangoproject.com/en/3.1/topics/db/queries/
    Query_comida = Registrogasto.objects.filter(category="Comida", owner="G")
    Query_despensa = Registrogasto.objects.filter(category="Despensa", owner="G")
    Query_servicios = Registrogasto.objects.filter(category="Servicios", owner="G")
    Query_extras = Registrogasto.objects.filter(category="Extras", owner="G")

    for query in Query_comida:
      xtotal_comida += query.quantity

    for query in Query_despensa:
      xtotal_despensa += query.quantity

    for query in Query_servicios:
      xtotal_servicios += query.quantity

    for query in Query_extras:
      xtotal_extras += query.quantity

    xtotal_neto = xtotal_comida + xtotal_despensa + xtotal_servicios + xtotal_extras

    dic_datostotales = {
        'total_comida' : xtotal_comida,
        'total_despensa' : xtotal_despensa,
        'total_servicios' : xtotal_servicios,
        'total_extras' : xtotal_extras,
        'total_neto': xtotal_neto
        }

    return dic_datostotales
