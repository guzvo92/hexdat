
#[ URLS / appmain0core]

from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [

    path('', views.index, name="index"),
    path('pelasputo/', views.pelasputo, name="pelasputo"),
]
