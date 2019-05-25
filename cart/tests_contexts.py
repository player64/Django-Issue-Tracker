from django.test import TestCase
from django.contrib.auth.models import User
from features.models import Features
from .contexts import number_items_in_cart


class TestContexts(TestCase):
    @staticmethod
    def create_feature(user):
        feature = Features(name='Test', description='Test desc', author=user)
        feature.save()
        return feature

    def setUp(self):
        self.user = User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')

    def test_context(self):
        self.assertEqual(number_items_in_cart(self.client)['cart_items'], 0)
        self.assertEqual(number_items_in_cart(self.client)['cart_total_price'], 0)
        feature = self.create_feature(self.user)
        response = self.client.post('/cart/add/{}'.format(feature.id), follow=True)
        self.assertEqual(response.context['cart_items'], 1)
        self.assertEqual(response.context['cart_total_price'], 50)
