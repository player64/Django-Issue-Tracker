from django.test import TestCase
from django.contrib.auth.models import User


class TestUserModels(TestCase):

    def test_string_username(self):
        entry = User(username="user")
        self.assertTrue(str(entry), entry.username)
