import os #para crear el salto de linea


def CreaUrlsAppz0projects(uri):

    file = open(uri, "w") #crea archivo
    file.close()  #limpiando archivo

    import0 = "#urls.py [appz0projects]"
    import1 = "#path ('projects/', include ('app.appz0projects.urls')),"
    import2 = "from django.urls import path"
    import3 = "from . import views"
    import4 = "from .views import *"
    import5 = "urlpatterns = [ "
    import6 = "     path('', views.index, name='index'),"
    import7 = "     ]"

    file = open(uri, "a") #append
    file.write("" +  import0 + "" + "\n")
    file.write("" +  import1 + "" + os.linesep)
    file.write("" +  import2 + "" + "\n")
    file.write("" +  import3 + "" + "\n")
    file.write("" +  import4 + "" + os.linesep)
    file.write("" +  import5 + "" + "\n")
    file.write("" +  import6 + "" + "\n")
    file.write("" +  import7 + "" + "\n")






    



