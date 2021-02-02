
#views.py [appmain1registration]

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy,reverse
from .models import Profile
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

    
#se actualizan los fields targeteando USER del get_object
@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    fields = [ 'avatar','bio','link'] #//del form.as_p
    template_name ='registration/profileform.html'
    success_url = reverse_lazy('profile')

    #este metodo es usado para extraer el USER que viende dentro de la request
    #//podemos saber el id del usuario sin pasarlo en el path
    def get_object(self): #//las updateview tienen metodo llamado getobject
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        #//este return me regresa una tupla (profile,created=tupla)
        print(profile.username)
        return profile























