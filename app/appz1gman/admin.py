#[ADMIN / Mysterys]

from django.contrib import admin
from .models import *

admin.site.register(Registroproyecto)

title = "Administrador General de modelos"
admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = "Panel de Gestion"
