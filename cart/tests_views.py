from django.test import TestCase
from django.contrib.auth.models import User
from features.models import Features


class TestViews(TestCase):
    @staticmethod
    def create_feature(user):
        feature = Features(name='Test', description='Test desc', author=user)
        feature.save()
        return feature

    def setUp(self):
        self.user = User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')

    # VIEW
    def test_cart_page_status(self):
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart.html')

    def test_cart_context(self):
        response = self.client.get('/cart/')
        self.assertEqual(len(response.context['cart']), 0)
        feature = self.create_feature(self.user)
        self.client.post('/cart/add/{}'.format(feature.id), follow=True)
        response = self.client.get('/cart/')
        cart_content = response.context['cart']
        self.assertEqual(len(cart_content), 1)
        self.assertEqual(cart_content[0]['name'], 'Test')

    # ADD
    def test_add_cart_status(self):
        feature = self.create_feature(self.user)
        response = self.client.post('/cart/add/{}'.format(feature.id))
        self.assertEqual(response.status_code, 301)

    def test_add_to_cart(self):
        feature = self.create_feature(self.user)
        self.client.post('/cart/add/{}'.format(feature.id), follow=True)
        session = self.client.session['cart']
        cart_items = len(session.keys())
        str_id = str(feature.id)
        self.assertTrue(str_id in session)
        self.assertEqual(cart_items, 1)
        self.assertEqual(session[str_id]['name'], 'Test')

    def test_add_to_cart_same_feature(self):
        feature = self.create_feature(self.user)
        self.client.post('/cart/add/{}'.format(feature.id), follow=True)
        str_id = str(feature.id)
        self.assertEqual(self.client.session['cart'][str_id]['qty'], 1)
        self.client.post('/cart/add/{}'.format(feature.id), follow=True)
        self.assertEqual(self.client.session['cart'][str_id]['qty'], 2)

    # DELETE
    def test_delete_cart_status(self):
        feature = self.create_feature(self.user)
        self.client.post('/cart/add/{}'.format(feature.id))
        response = self.client.post('/cart/delete/{}'.format(feature.id), follow=True)
        self.assertContains(response, 'Successfully deleted item from the cart', 1, 200)

    def test_delete_from_cart(self):
        feature = self.create_feature(self.user)
        self.client.post('/cart/add/{}'.format(feature.id), follow=True)
        self.assertEqual(len(self.client.session['cart'].keys()), 1)
        response = self.client.post('/cart/delete/{}'.format(feature.id), follow=True)
        self.assertEqual(len(self.client.session['cart'].keys()), 0)
        self.assertContains(response, 'Successfully deleted item from the cart', 1, 200)
