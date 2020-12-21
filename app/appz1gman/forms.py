from django.core import validators
from django.contrib.auth.forms import UserCreationorm
from django .contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','pass1','pass2']
