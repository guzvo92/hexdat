#urls.py [appz0projects]
#path ('projects/', include ('app.appz0projects.urls')),

from django.urls import path
from . import views
from .views import *
from app.appmain1registration.views import * #importeilustrativo

urlpatterns = [
    path('', ProjectListlView.as_view(), name="listproy"),
    path('create/', ProjectCreate.as_view(), name='createproy'),
]
