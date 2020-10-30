
#[ URLS / appx1moneytrack]

from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [

    path('', views.index_moneytrack, name="index_moneytrack"),
]
