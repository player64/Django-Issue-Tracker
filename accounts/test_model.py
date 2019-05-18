from django.test import TestCase
from django.contrib.auth.models import User


class TestUserModels(TestCase):

    def authenticate(self):
        user = User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')
        
    def test_user_login(self):
        pass