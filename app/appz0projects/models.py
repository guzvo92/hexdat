#[models appz0projects]

from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    details = models.TextField(null=True, blank=True)



