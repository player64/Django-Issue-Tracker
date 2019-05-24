from django.test import TestCase
from .models import Bugs, BugComment


class TestBugModel(TestCase):

    def test_bug_name(self):
        bug = Bugs(name='Test', description='description',
                   author_id=1)
        self.assertEqual(Bugs.__str__(bug), 'Test')

    def test_bug_creation(self):
        bug = Bugs(name='Test', description='description',
                   author_id=1)

        self.assertEqual(bug.name, 'Test')
        self.assertEqual(bug.description, 'description')
        self.assertEqual(bug.status, 'todo')
        self.assertEqual(bug.views, 0)
        self.assertEqual(bug.author_id, 1)

    def test_comment_name(self):
        comment = BugComment(comment='Hey', bug_id=1, author_id=1)
        self.assertEqual(BugComment.__str__(comment), 'Hey')

    def test_comment(self):
        comment = BugComment(comment='Hey', bug_id=1, author_id=1)
        self.assertEqual(comment.comment, 'Hey')
        self.assertEqual(comment.bug_id, 1)
        self.assertEqual(comment.author_id, 1)
