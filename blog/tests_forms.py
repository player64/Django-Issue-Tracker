from django.test import TestCase
from .forms import PostCommentForm


class TestPostForms(TestCase):

    def test_bug_comment_form_correct(self):
        form = PostCommentForm({
            'comment': 'This is a comment'
        })
        self.assertTrue(form.is_valid())

    def test_bug_comment_form_empty_comment(self):
        form = PostCommentForm({
            'comment': ''
        })
        self.assertFalse(form.is_valid())
