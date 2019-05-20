from django.test import TestCase
from django.contrib.auth.models import User
# https://realpython.com/testing-in-django-part-1-best-practices-and-examples/


class TestUserViews(TestCase):

    def authenticate(self):
        User.objects.create_user(username='username', password='password')
        return self.client.login(username='username', password='password')

    def test_check_valid_login(self):
        auth_user = self.authenticate()
        self.assertTrue(auth_user)
        response = self.client.get('/', follow=True)
        self.assertEqual(str(response.context['user']), 'username')

    def test_login_form_validation(self):
        response = self.client.post('/accounts/login/', {'email': 'test@test'})
        self.assertContains(response, 'This field is required.', 1, 200)
        self.assertFormError(response, 'form', 'email', u'Enter a valid email address.')

    def test_registration_email_taken(self):
        data = {
            'email': 'test@test.com',
            'username': 'test',
            'password1': 'password',
            'password2': 'password'
        }
        User.objects.create_user(username='test', email=data['email'], password='password')
        response = self.client.post('/accounts/register/', data, follow=True)
        self.assertFormError(response, 'form', 'email', u'Email addresses is already registered.')

    def test_login_page(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_registration_page(self):
        response = self.client.get('/accounts/register/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_login_redirection_when_authenticated(self):
        self.authenticate()
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 302)

    def test_logout(self):
        self.authenticate()
        response = self.client.get('/accounts/logout/')
        self.assertEqual(response.status_code, 302)

    def test_logout_response_message(self):
        self.authenticate()
        response = self.client.get('/accounts/logout/', follow=True)
        self.assertContains(response, 'You have successfully logged out', 1, 200)

    def test_profile_page(self):
        self.authenticate()
        response = self.client.get('/accounts/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')
