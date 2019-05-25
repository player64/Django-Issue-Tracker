from django.test import TestCase
from .utilis import month_names, get_month_name


class TestCheckoutUtilis(TestCase):

    def test_month_names(self):
        self.assertEqual(month_names()[1], 'January')

    def test_get_month_name(self):
        self.assertEqual(get_month_name(12), 'December')

    def test_get_month_name_wrong(self):
        self.assertFalse(get_month_name(13))
