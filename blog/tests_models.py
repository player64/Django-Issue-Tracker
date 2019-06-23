from django.test import TestCase
from .models import Post, PostComment


class TestFeaturesModel(TestCase):

    def test_feature_name(self):
        feature = Post(name='Test', description='description')
        self.assertEqual(Post.__str__(feature), 'Test')

    def test_feature_creation(self):
        feature = Post(name='Test', description='description')
        self.assertEqual(feature.name, 'Test')
        self.assertEqual(feature.description, 'description')

    def test_comment_name(self):
        comment = PostComment(comment='Hey', post_id=1, author_id=1)
        self.assertEqual(PostComment.__str__(comment), 'Hey')

    def test_comment(self):
        comment = PostComment(comment='Hey', post_id=1, author_id=1)
        self.assertEqual(comment.comment, 'Hey')
        self.assertEqual(comment.post_id, 1)
        self.assertEqual(comment.author_id, 1)
