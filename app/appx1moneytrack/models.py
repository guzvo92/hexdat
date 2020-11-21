from django.db import models

# Create your models here.


class Registrogasto(models.Model):
    quantity = models.IntegerField(default='0')
    concept = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    created_at= models.DateTimeField(auto_now_add=True)
