from django.test import TestCase
import json
from bugs.models import Bugs
from features.models import Features
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

    # API
    def test_api_stats_status(self):
        response = self.client.post('/api/stats/', content_type='application/json')
        response_data = json.loads(str(response.content, encoding='utf8'))
        self.assertEqual(response_data['statuses']['features']['done'], 0)

    def test_api_with_correct_count(self):
        Features(name='Test', author_id=1, status='done').save()
        response = self.client.post('/api/stats/', content_type='application/json')
        response_data = json.loads(str(response.content, encoding='utf8'))
        self.assertEqual(response_data['statuses']['features']['done'], 1)

    def test_api_with_names(self):
        for item in range(1, 12):
            bug = Bugs(name='Test_{}'.format(item), author_id=1, total_votes=item*2)
            bug.save()

        response = self.client.post('/api/stats/', content_type='application/json')
        response_data = json.loads(str(response.content, encoding='utf8'))
        self.assertTrue('votes' in response_data)
        self.assertTrue('bugs' in response_data['votes'])
        self.assertEqual(len(response_data['votes']['bugs']['labels']), 10)

    def test_create_voted_items(self):
        from .views import create_voted_items
        bugs = []
        for item in range(0, 10):
            bug = Bugs(name='Test_{}'.format(item), author_id=1, total_votes=item)
            bugs.append(bug)

        created_list = create_voted_items(bugs)

        self.assertTrue('labels' in created_list)
        self.assertTrue('votes' in created_list)
        self.assertEqual(len(created_list['votes']), 10)
        self.assertEqual(len(created_list['labels']), 10)
