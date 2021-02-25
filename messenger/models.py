#models.py [messenger]

from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

class Thread(models.Model):
    #el lugar almacena los usuarios y los mensajes
    #para acceder con user.threads
    users = models.ManyToManyField(User, related_name='threads')
    #le pasariamos el modelo messages
    #y almacenariamos todos los mensajes que forman parte del hilo
    messages = models.ManyToManyField(Message)


#Para evaluar mensajes y que usuarios si estan en el hilo
from django.db.models.signals import m2m_changed
#conjunto = lista pero sin elementos duplicados
def messages_changed(sender, **kwargs):
    #el pop saca el elemento del diccionario, si no la ecuentra que devuelva NONE
    instance = kwargs.pop("instance",None) #recupera el hilo donde se ejecuta
    action = kwargs.pop("action",None) #detecta accion ejecutada el post y pre /add
    pk_set = kwargs.pop("pk_set",None) #recupera un conjunto con el identificador de cada mensage
    print(instance, action, pk_set)

    #para borrar lo que no este dentro de los 2usuarios permitidos
    #como no se puede eliminar contenido durante una iteracion:
    false_pk_set = set()
    if action is "pre_add":
        for msg_pk in pk_set:
            msg= Message.objects.get(pk=msg_pk)
            if msg.user not in instance.users.all():
                print("Ups ({}) no forma parte del hilo".format(msg.user))
                false_pk_set.add(msg_pk) #se agregara mensaje y al final se comparara

    #Buscar los mensajes que si estan en pk_set
    pk_set.difference_update(false_pk_set) #metodo de los CONJUNTOS


#para conectarla con cualquier cambio que aparezca en el campo M2M Messages
m2m_changed.connect(messages_changed, sender=Thread.messages.through)


#python manage.py test messenger.tests.ThreadTestCase.test_add_message_from_user_not_in_thread
