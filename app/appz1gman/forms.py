from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django .contrib.auth.models import User

from .models import *

#class RegisterForm(UserCreationForm):
    #class Meta:
      #  model = User
       # fields = ['username','email','pass1','pass2']


from django import forms

class UploadDocumentForm(forms.ModelForm):
    class Meta:
        model= Apiuploadmod
        fields = ['title','file']
    
    #file = forms.FileField()
    #image = forms.ImageField()