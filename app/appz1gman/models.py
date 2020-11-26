#[ Models / appz1gman]
from django.db import models

# Create your models here.

class Registroproyecto(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    mainimage = models.ImageField(default='null',upload_to ="projects")
    image1 = models.ImageField(default='null')
    image2 = models.ImageField(default='null')
    image3 = models.ImageField(default='null')
    image4 = models.ImageField(default='null')
    image5 = models.ImageField(default='null')
    created_at = models.DateTimeField(auto_now_add=True, editable=False )
    updated_at = models.DateTimeField(auto_now=True)

    #created_at= models.DateTimeField(auto_now_add=True)
    #updated_at = models.DateTimeField(auto_now=True)
