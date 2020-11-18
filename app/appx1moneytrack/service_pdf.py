
#INSTALAR pip install reportlab
import os
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from django.http import HttpResponse
from .services import *
from .models import *


def report_fn():

    registros = Registrogasto.objects.all()
    datostotales = totalgastos()

    #creando los httpresponse headers con pdf
    #response = HttpResponse("hello world")
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=Reporte_Gastos.pdf'

    #Creater el objeto pdf usando el "objeto BytesIO" como archivo
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)

    #creando los headers
    c.setLineWidth(.3)
    c.setFont('Helvetica',22)
    c.drawString(30,750,'Reporte de gastos')
    c.setFont('Helvetica-Bold',12)
    c.drawString(480,750, "01/11/2020")
    c.line(460,747,560,747) #(x,height,y,height)

    x=50
    y=700
    count = 1

    for reg in registros:
        fecha_cut = (str(reg.created_at)[0:16])

        c.drawString(x,y, str(count) )
        x += 20
        c.drawString(x,y, str(reg.quantity) )
        x += 40
        c.drawString(x,y, str(reg.category) )
        x += 100
        c.drawString(x,y, str(reg.concept))
        x += 200
        c.drawString(x,y, str(fecha_cut))
        y -= 50
        x = 50
        count += 1

    c.save()

    pdf =buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response
