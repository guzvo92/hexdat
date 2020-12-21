
#[ models / appmain1admin]
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Nota(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
