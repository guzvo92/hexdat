#[ URLS / appx1moneytrack]

from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [

    path('', views.index_moneytrack_pub, name="index_moneytrack_pub"),
    path('all/', views.index_moneytrack_all, name="index_moneytrack_all"),
    path('save_formoney_reg/', views.save_formoney_reg, name="saveformoneyreg"),
    path('clear_form_reg/<int:idx>', views.clear_form_reg, name="clearformreg"),
    path('reportpub/', views.reportpub, name="report"),
    path('reportall/', views.reportall, name="reportall"),
]
