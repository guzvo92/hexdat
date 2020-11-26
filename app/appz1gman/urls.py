#[ URLS / appz1gman]

from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [

    path('', views.index_gman, name="index_gman"),
    path('admin/', views.admin_gman, name="admin_gman"),
    path('save_project/', views.save_project, name="save_project"),
    path('clear_project/<int:idx>', views.clear_project, name="clear_project"),
    path('edit_project/<int:idx>', views.edit_project, name="edit_project"),
    path('save_edit_project/<int:idx>', views.save_edit_project, name="save_edit_project"),

]
