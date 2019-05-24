from django.test import TestCase
from .models import Features, FeatureComment


class TestFeaturesModel(TestCase):

    def test_feature_name(self):
        feature = Features(name='Test', description='description', author_id=1)
        self.assertEqual(Features.__str__(feature), 'Test')

    def test_feature_creation(self):
        feature = Features(name='Test', description='description', author_id=1)
        self.assertEqual(feature.name, 'Test')
        self.assertEqual(feature.description, 'description')
        self.assertEqual(feature.status, 'todo')
        self.assertEqual(feature.views, 0)
        self.assertEqual(feature.paid_no, 0)
        self.assertEqual(feature.author_id, 1)

    def test_comment_name(self):
        comment = FeatureComment(comment='Hey', feature_id=1, author_id=1)
        self.assertEqual(FeatureComment.__str__(comment), 'Hey')

    def test_comment(self):
        comment = FeatureComment(comment='Hey', feature_id=1, author_id=1)
        self.assertEqual(comment.comment, 'Hey')
        self.assertEqual(comment.feature_id, 1)
        self.assertEqual(comment.author_id, 1)
