from django.test import TestCase

from .models import Profile
from django.contrib.auth.models import User

class ProfileTestCase(TestCase):
    def setUP(self):
        User.objects.create_user('test','test@test.com','test1234')

    def test_profile_exists(self):
        #Busca el profile con el username test
        exists = Profile.objects.filter(user__username='test').exists()
        #comparar que exist debe ser TRUE
        self.assertEqual(exists,True)

#se ejecuta con el manage
#> python manage.test appmain1registration
