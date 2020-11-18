#INSTALAR pip install reportlab
import os
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from django.http import HttpResponse

def report(request):

	response = HttpResponse("hello world")
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename=ReporteGli.pdf'

	buffer = BytesIO()
	c = canvas.Canvas(buffer, pagesize=A4)

	c.setLineWidth(.3)
	c.setFont('Helvetica',22)
	c.drawString(30,750,'GMAN')
	c.save()

	pdf =buffer.getvalue()
	buffer.close()
	response.write(pdf)

	return response

#FUNCIONANDO!!!!!!!!!!!!!!!!!!
