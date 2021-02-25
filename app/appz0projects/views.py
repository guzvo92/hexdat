#views.py [appz0projects]
#CreaUrlsAppz0projects("app/appz0projects/segmentados/urls.py")

from django.shortcuts import render
from .segmentados.makers import *

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from app.appmain1registration.models import Profile
from django.shortcuts import get_object_or_404
from app.appz0projects.models import Project
from django.urls import reverse_lazy,reverse
from django import forms

#methods
#Con esto me crea un RECORD con el USUARIO actual logueado
#ligado al modelo con una foreing key
@method_decorator(login_required, name='dispatch')
class ProjectCreate(CreateView):
    model = Project
    fields = ['title','description','details']
    template_name ='appz0projects/project_create.html'
    success_url = reverse_lazy('createproy')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super(ProjectCreate, self).get_form()
        #modificar en tiempo real

        form.fields['title'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Titulo'})
        form.fields['description'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Descripcion'})
        form.fields['details'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Detalles'})
        #//puedes esconder las labels asi o editando el css en html label:display:none
        #form.fields['username'].label =""
        return form

#el problema con  el DETAILVIEW es que me filtra los 3 proyectos
#pero por ser detailview solo acepta un query

''' //FORMA SIMPLE:
class ProjectListlView(ListView):
    model = Project
    template_name = 'appz0projects/project_list.html'
    #paginate_by = 3

    //HAY QUE AGREGARLE ESTA CONDICION despues del for
    {% if project.user_id == request.user.id  %}
    {% endif %}
'''

@method_decorator(login_required, name='dispatch')
class ProjectListlView(ListView):
    model = Project
    template_name = 'appz0projects/project_list.html'
    #paginate_by = 3

    def get_queryset(self):
        queryset = super(ProjectListlView, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset
