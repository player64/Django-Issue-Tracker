from django.test import TestCase
from .forms import UserLoginForm, UserRegistrationForm


class TestUserForms(TestCase):

    def test_login_with_correct_values(self):
        form = UserLoginForm({
            'email': 'test@test.com',
            'password': 'test_password'
        })
        self.assertTrue(form.is_valid())

    def test_valid_login_form(self):
        form = UserLoginForm({
            'email': 'test@test.com',
            'password': 'test_password'
        })
        self.assertTrue(form.is_valid())

    def test_login_with_wrong_email(self):
        form = UserLoginForm({
            'email': 'test@test',
            'password': 'test_password'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('Enter a valid email address.', form.errors['email'])

    def test_registration_with_valid_data(self):
        form = UserRegistrationForm({
            'email': 'test@test.com',
            'username': 'tester',
            'password1': 'password',
            'password2': 'password'
        })
        self.assertTrue(form.is_valid())

    def test_registration_with_wrong_email_and_empty_username(self):
        form = UserRegistrationForm({
            'email': 'test@test'
        })

        self.assertIn('Enter a valid email address.', form.errors['email'])
        self.assertIn('This field is required.', form.errors['username'])
        self.assertIn('This field is required.', form.errors['password1'])
        self.assertIn('This field is required.', form.errors['password2'])

    def test_registration_not_password_equal(self):
        form = UserRegistrationForm({
            'email': 'test@test.com',
            'username': 'tester',
            'password1': 'password',
            'password2': 'password2'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('Passwords do not match', form.errors['password2'])
