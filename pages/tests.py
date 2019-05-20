from django.test import TestCase
# Create your tests here.


class TestPagesViews(TestCase):

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_about_page(self):
        response = self.client.get('/about-us/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_stats_page(self):
        response = self.client.get('/stats/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stats.html')
