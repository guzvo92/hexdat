
#INSTALAR pip install reportlab
import os
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from django.http import HttpResponse
from .services import *
from .models import *
from datetime import datetime, timedelta


def report_fn(type,registros, datostotalesx): 

    #print(datostotalesx.get(total_comida))
    #print(datostotalesx.total_despensa)

    tiemponow = (datetime.today()).strftime("%d-%m-%y %H:%M")
    namepdf = "R[" + type +"]" + str(tiemponow) 
    titulo = "Reporte de Gastos "+ type

    #creando los httpresponse headers con pdf
    #response = HttpResponse("hello world")
    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename=Reporte_Gastos.pdf'
    response['Content-Disposition'] = 'attachment; filename='+ namepdf +'.pdf'

    #Creater el objeto pdf usando el "objeto BytesIO" como archivo
    buffer = BytesIO()
    image = 'static/appx1moneytrack/logohexdat_white.png'
    c = canvas.Canvas(buffer, pagesize=A4)

    #creando los headers
    c.drawInlineImage(image, 40, 745, 100, 30)
    c.setLineWidth(.3)
    c.setFont('Helvetica',22)
    c.drawString(170,750,titulo)
    c.setFont('Helvetica-Bold',12)
    c.drawString(450,750, str(tiemponow)  )
    c.line(430,747,550,747) #(xini,yini,xfin,yfin)

    #haciendo el bloque de indicadores

    CO1x = [ 50 , 150,  250, 360, 450]

    c.drawString(CO1x[0],700,"Comida")
    c.drawString(CO1x[1],700,"Despensa")
    c.drawString(CO1x[2],700,"Servicios")
    c.drawString(CO1x[3],700,"Extras")
    c.drawString(CO1x[4],700,"Total Gastos")

    CO2x = [ 64 , 165,  268, 365, 475]

    c.drawString(CO2x[0],680,str(datostotalesx.get("total_comida")))
    c.drawString(CO2x[1],680,str(datostotalesx.get("total_despensa")))
    c.drawString(CO2x[2],680,str(datostotalesx.get("total_servicios")))
    c.drawString(CO2x[3],680,str(datostotalesx.get("total_extras")))
    c.drawString(CO2x[4],680,str(datostotalesx.get("total_neto")))

    #desplegando los registros
    x=50
    y=600
    count = 1
    for reg in registros:
        fecha_cut = (str(reg.created_at)[0:16])

        c.drawString(x,y, str(count) )
        x += 40
        c.drawString(x,y, str(reg.quantity) )
        x += 40
        c.drawString(x,y, str(reg.category) )
        x += 120
        c.drawString(x,y, str(reg.concept))
        x += 200
        c.drawString(x,y, str(fecha_cut))
        y -= 30
        x = 50
        count += 1

    c.save()

    pdf =buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response
