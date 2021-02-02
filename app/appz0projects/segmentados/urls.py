#urls.py [appz0projects]
#path ('projects/', include ('app.appz0projects.urls')),
from django.urls import path
from . import views
from .views import *
urlpatterns = [ 
     path('', views.index, name='index'),
     ]
