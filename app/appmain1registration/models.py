#[models appmain1registration]

from django.db import models
from django.contrib.auth.models import User

#para sobrescribir ultima imagen cargada de un usuario
def custom_upload_to(instance,filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/' + filename

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    alias = models.TextField()
    #avatar = models.ImageField(upload_to="profiles", null=True, blank=True)
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)

    #para ordenar los datos en el listview de profiles
    #por nombres
    class Meta:
        ordering = ['user__username']


from django.dispatch import receiver
from django.db.models.signals import post_save

#//SIGNALS
#para targetear el modelo User despues de creado
@receiver(post_save, sender=User)#post-pre/save post-pre/delete
def ensure_profile_exist(sender, instance, **kwargs):

    if kwargs.get('created',False): #si existe esta clave
    #entonces se ha creado por primera vez
        Profile.objects.get_or_create(user=instance)
        print("[SIGNAL]Se creo usuario y perfil enlazado")
