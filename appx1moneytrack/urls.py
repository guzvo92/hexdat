
#[ URLS / appx1moneytrack]

from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [

    path('', views.index_moneytrack, name="index_moneytrack"),
    path('save_formoney_reg/', views.save_formoney_reg, name="saveformoneyreg"),
    path('clear_form_reg/<int:idx>', views.clear_form_reg, name="clearformreg"),
]
