#[ Models / appz1gman]
from django.db import models

# Create your models here.

class Registroproyecto(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=150)
    details = models.CharField(default='null', max_length=500)
    category = models.CharField(default='null', max_length=100)
    image1 = models.ImageField(default='null',upload_to ="projectsgman")
    image2 = models.ImageField(default='null',upload_to ="projectsgman")
    image3 = models.ImageField(default='null',upload_to ="projectsgman")
    image4 = models.ImageField(default='null',upload_to ="projectsgman")
    image5 = models.ImageField(default='null',upload_to ="projectsgman")
    created_at = models.DateTimeField(auto_now_add=True, editable=False )
    updated_at = models.DateTimeField(auto_now=True)

    #created_at= models.DateTimeField(auto_now_add=True)
    #updated_at = models.DateTimeField(auto_now=True)
