
#INSTALAR pip install reportlab
import os
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from django.http import HttpResponse


def report_fn():

    #creando los httpresponse headers con pdf
    #response = HttpResponse("hello world")
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=ReporteGli.pdf'

    #Creater el objeto pdf usando el "objeto BytesIO" como archivo
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)

    #creando los headers
    c.setLineWidth(.3)
    c.setFont('Helvetica',22)
    c.drawString(30,750,'GMAN')
    c.setFont('Helvetica-Bold',12)
    c.drawString(480,750, "01/11/2020")
    c.line(460,747,560,747) #(x,height,y,height)
    c.save()

    pdf =buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response
