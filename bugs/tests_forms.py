from django.test import TestCase
from .forms import BugForm, BugCommentForm


class TestBugsForms(TestCase):

    def test_bug_form_with_correct_values(self):
        form = BugForm({
            'name': 'Bug',
            'description': 'Bug description'
        })
        self.assertTrue(form.is_valid())

    def test_bug_form_with_empty_values(self):
        form = BugForm({
            'name': '',
            'description': 'Bug description'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('This field is required.', form.errors['name'])

    def test_bug_form_with_long_name(self):
        form = BugForm({
            'name': 'Sometimes, all you need to do is completely make an ass of yourself and laugh it off to'
                    ' realise that life isn’t so bad after all.',
            'description': 'Bug description'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('Ensure this value has at most 50 characters ', str(form.errors['name']))

    def test_bug_comment_form_correct(self):
        form = BugCommentForm({
            'comment': 'This is a comment'
        })
        self.assertTrue(form.is_valid())

    def test_bug_comment_form_empty_comment(self):
        form = BugCommentForm({
            'comment': ''
        })
        self.assertFalse(form.is_valid())
