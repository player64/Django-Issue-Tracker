from django.test import TestCase
from django.contrib.auth.models import User
from .backends import EmailAuth


class TestBackendAuth(TestCase):

    def test_email_valid_authentication(self):
        User.objects.create_user(username='username', email='test@test.com', password='password')
        user = EmailAuth.authenticate(email='test@test.com', password='password')

        self.assertEqual(user.username, 'username')
        self.assertEqual(user.email, 'test@test.com')

    def test_email_authentication_not_valid_credentials(self):
        EmailAuth.authenticate(email='test@test.com', password='password')
        self.failureException(User.DoesNotExist)

    def test_email_authentication_wrong_password(self):
        User.objects.create_user(username='username', email='test@test.com', password='password')
        user = EmailAuth.authenticate(email='test@test.com', password='pass')
        self.assertIsNone(user)

    def test_get_user_valid(self):
        create_user = User.objects.create_user(username='username', email='test@test.com', password='password')
        get_user = EmailAuth.get_user(create_user.id)
        self.assertEqual(get_user.username, 'username')
        self.assertEqual(get_user.email, 'test@test.com')

    def test_get_user_not_active(self):
        create_user = User.objects.create_user(username='username', email='test@test.com',
                                               password='password', is_active=False)
        get_user = EmailAuth.get_user(create_user.id)
        self.assertIsNone(get_user)

    def test_get_user_not_valid_credentials(self):
        EmailAuth.get_user(2)
        self.failureException(User.DoesNotExist)