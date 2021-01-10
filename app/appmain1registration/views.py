
#views.py [appmain1registration]



#form generico
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

from django import forms

class SignUpView(CreateView):
    form_class = UserCreationForm
    #success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def get_success_url(self):
        #concatenamos por get para indicar que se registro
        return reverse_lazy('login') + '?xregister'

    #funcion para sobreescribir un widget en timpo de ejecucion
    #primero se buscan las labels con ctl+u <find> "name"
    def get_form(selft, form_class=None):
        form = super(SignUpView, selft).get_form()
        #modificar en tiempo real
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Nombre de usuario'})
        form.fields['password1'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Password'})
        form.fields['password2'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Repite el Password'})
        #//puedes esconder las labels asi o editando el css en html label:display:none
        #form.fields['username'].label =""
        return form




















