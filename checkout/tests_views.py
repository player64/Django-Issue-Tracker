from django.test import TestCase
from django.contrib.auth.models import User
from features.models import Features


class TestViews(TestCase):

    @staticmethod
    def create_feature(user):
        feature = Features(name='Test', description='Test desc', author=user)
        feature.save()
        return feature

    @staticmethod
    def card_type(type):
        card_types = {
            'valid': {
                'number': '4000000000000077',
                'token': 'tok_visa',
            },
            'no_funds': {
                'number': '4000000000009995',
                'token': 'tok_chargeDeclinedInsufficientFunds'
            },
            'declined': {
                'number': '4000000000000002',
                'token': 'tok_chargeDeclined'
            }
        }
        return card_types[type] if type in card_types else False

    def buyer_data(self, card_type):
        card = self.card_type(card_type)
        return {
            'full_name': 'Test test',
            'phone_number': '088 888 88 88',
            'country': 'Ireland',
            'postcode': 'RD1111',
            'town_or_city': 'Dublin',
            'street_address1': 'Example street',
            'street_address2': None,
            'county': 'Dublin',
            'credit_card_number': card['number'],
            'cvv': "111",
            'expiry_month': 1,
            'expiry_year': 2020,
            'stripe_id': card['token']
        }

    def create_checkout(self):
        feature = self.create_feature(self.user)
        self.client.post('/cart/add/{}'.format(feature.id), follow=True)

    def setUp(self):
        self.user = User.objects.create_user(username='username', email='test@test@.com',
                                             password='password')
        self.client.login(username='username', password='password')

    def test_checkout_status_and_template_used(self):
        self.create_checkout()
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout.html')

    def test_empty_checkout_redirection(self):
        response = self.client.get('/checkout/', follow=True)
        self.assertContains(response, 'Your cart is empty', 1, 200)

    def test_success_payments(self):
        self.create_checkout()
        response = self.client.post('/checkout/', data=self.buyer_data('valid'), follow=True)
        self.assertContains(response, 'You have successfully paid', 1, 200)

    def test_insufficient_funds_payment(self):
        self.create_checkout()
        response = self.client.post('/checkout/', data=self.buyer_data('no_funds'), follow=True)
        self.failureException(Exception)
        self.assertContains(response, 'Your card was declined!', 1, 200)

    def test_declined_payment(self):
        self.create_checkout()
        response = self.client.post('/checkout/', data=self.buyer_data('declined'), follow=True)
        self.failureException(Exception)
        self.assertContains(response, 'Your card was declined!', 1, 200)

    def test_no_valid_form(self):
        self.create_checkout()
        response = self.client.post('/checkout/', data={}, follow=True)
        self.assertContains(response, 'We were unable to take a payment with that card!', 1, 200)