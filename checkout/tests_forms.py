from django.test import TestCase
from .forms import PaymentForm, OrderForm


class TestForm(TestCase):

    def test_payment_form_correct_values(self):
        form = PaymentForm({
            'credit_card_number': '4242424242424242',
            'cvv': "111",
            'expiry_month': 1,
            'expiry_year': 2020,
            'stripe_id': 'l'
        })
        self.assertTrue(form.is_valid())

    def test_payment_form_not_correct(self):
        form = PaymentForm({
            'credit_card_number': '4242424242424242',
            'cvv': "111",
            'expiry_month': None,
            'expiry_year': '',
            'stripe_id': 'l'
        })
        self.assertFalse(form.is_valid())

    def test_order_form_correct_values(self):
        form = OrderForm({
            'full_name': 'Test test',
            'phone_number': '088 888 88 88',
            'country': 'Ireland',
            'postcode': 'RD1111',
            'town_or_city': 'Dublin',
            'street_address1': 'Example street',
            'street_address2': None,
            'county': 'Dublin'
        })
        self.assertTrue(form.is_valid())

    def test_order_form_incorrect_values(self):
        form = OrderForm({
            'full_name': None,
            'phone_number': '088 888 88 88',
            'country': 'Ireland',
            'postcode': 'RD1111',
            'town_or_city': 'Dublin',
            'street_address1': 'Example street',
            'street_address2': 'Example street',
            'county': None
        })
        self.assertFalse(form.is_valid())