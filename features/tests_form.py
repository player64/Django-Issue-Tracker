from django.test import TestCase
from .forms import FeatureForm, FeatureCommentForm


class TestFeaturesForms(TestCase):

    def test_feature_form_with_correct_values(self):
        form = FeatureForm({
            'name': 'Feature',
            'description': 'Feature description'
        })
        self.assertTrue(form.is_valid())

    def test_feature_form_with_empty_values(self):
        form = FeatureForm({
            'name': '',
            'description': 'Feature description'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('This field is required.', form.errors['name'])

    def test_feature_form_with_long_name(self):
        form = FeatureForm({
            'name': 'Sometimes, all you need to do is completely make an ass of yourself and laugh it off to'
                    ' realise that life isn’t so bad after all.',
            'description': 'Feature description'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('Ensure this value has at most 50 characters ', str(form.errors['name']))

    def test_feature_comment_form_correct(self):
        form = FeatureCommentForm({
            'comment': 'This is a comment'
        })
        self.assertTrue(form.is_valid())

    def test_feature_comment_form_empty_comment(self):
        form = FeatureCommentForm({
            'comment': ''
        })
        self.assertFalse(form.is_valid())
