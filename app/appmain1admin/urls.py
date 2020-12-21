#[ URLS / appmain1admin]
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [

    path('', views.no, name="no"),

   
    path('register/', views.register_page, name="register"),
    path('profile/', views.profile_page, name="profile"),
    path('login/', views.login_page, name="login"),
    
]


