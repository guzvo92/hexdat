from django.test import TestCase
from django.contrib.auth.models import User

from .models import Thread,Message
# Create your tests here.

class ThreadTestCase(TestCase):
    def setUp(self):
        self.usera = User.objects.create_user('usera',None,'nkgc69mk')
        self.userb = User.objects.create_user('userb',None,'nkgc69mk')
        self.userc = User.objects.create_user('userc',None,'nkgc69mk')
        self.thread = Thread.objects.create()

    #test sencillo que agrega 2 usuarios y luego los compara con 2con asercion
    def test_add_users_to_thread(self):
        #hacer referencia al campo del modelo MTM users (que espera usuarios)
        #metodo add para asignarles objetos sep x comas
        self.thread.users.add(self.usera, self.userb)
        #se crea una asercion que comprobaria si 2 valores son equivalentes
        #comprueba si hay 2 usuarios dentro del hilo
        self.assertEqual(len(self.thread.users.all()),2)

    #test para evluar que no hay dos hilos con los mismos usuarios
    def test_filter_thread_by_users(self):
        self.thread.users.add(self.usera, self.userb)
        #obtener los treads donde esta el usuario a y el usuario b
        threads = Thread.objects.filter(users=self.usera).filter(users=self.userb)
        #multifiltro gracias a que es un queryset
        #comparar el hilo del selft thread y el hilo de la 1era posicion
        self.assertEqual(self.thread, threads[0])

    #test comprobar que no existe un hilo cunado los usuarios no forman parte de el
    def test_filter_non_existent_thread(self):
        threads = Thread.objects.filter(users=self.usera).filter(users=self.userb)
        self.assertEqual(len(threads),0)

    def test_add_message_to_thread(self):
        self.thread.users.add(self.usera, self.userb)
        message1 = Message.objects.create(user=self.usera, content="muy buenas")
        message2 = Message.objects.create(user=self.userb, content="hola")
        self.thread.messages.add(message1,message2)
        self.assertEqual(len(self.thread.messages.all()),2)

        for message in self.thread.messages.all():
            print("({}):{}".format(message.user, message.content))

    def test_add_message_from_user_not_in_thread(self):
        self.thread.users.add(self.usera, self.userb)
        message1 = Message.objects.create(user=self.usera, content="muy buenas")
        message2 = Message.objects.create(user=self.userb, content="hola")
        message3 = Message.objects.create(user=self.userc, content="Soy un espia")
        self.thread.messages.add(message1,message2,message3)
        self.assertEqual(len(self.thread.messages.all()),2)

#recordar que para cada test independiente se ejecuta el setUp

#SE EJECUTA > python manage.py test messenger
#SE EJECUTA > python manage.py test messenger.tests.ThreadTestCase
#SE EJECUTA > python manage.py test messenger.tests.ThreadTestCase.test_add_users_to_thread
