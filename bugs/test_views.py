from django.test import TestCase
from django.contrib.auth.models import User
from .models import Bugs, BugComment


class TestViews(TestCase):

    @staticmethod
    def create_other_user():
        return User.objects.create_user(username='other_user', password='password')

    @staticmethod
    def create_bug(user):
        bug = Bugs(
            name='Test', description='Test desc', author=user
        )
        bug.save()
        return bug

    def setUp(self):
        self.user = User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')

    # ARCHIVE
    def test_archive_page_status(self):
        response = self.client.get('/bugs/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'archive.html')

    # SINGLE
    def test_single_page_status(self):
        user = self.create_other_user()
        bug = self.create_bug(user)
        response = self.client.get('/bugs/{}/'.format(bug.id))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'single.html')

    # VOTE
    def test_vote_and_un_vote(self):
        user = self.create_other_user()
        bug = self.create_bug(user)
        self.client.post('/bugs/vote/{}/'.format(bug.id))
        bug.refresh_from_db()
        self.assertEqual(len(bug.voted_by.values_list()), 1)
        response = self.client.post('/bugs/vote/{}/'.format(bug.id))
        bug.refresh_from_db()
        self.assertEqual(len(bug.voted_by.values_list()), 0)
        self.assertEqual(response.status_code, 302)

    def test_vote_on_own_recipe(self):
        bug = self.create_bug(self.user)
        response = self.client.post('/bugs/vote/{}/'.format(bug.id), follow=True)
        bug.refresh_from_db()
        self.assertEqual(len(bug.voted_by.values_list()), 0)
        self.assertContains(response, "You cannot vote for own bug", 1, 200)

    # DELETE
    def test_delete_bug(self):
        bug = self.create_bug(self.user)
        self.client.post('/bugs/delete/{}/'.format(bug.id), follow=True)
        count_bugs = Bugs.objects.count()
        self.assertEqual(count_bugs, 0)

    def test_delete_someone_bug(self):
        user = self.create_other_user()
        bug = self.create_bug(user)
        response = self.client.post('/bugs/delete/{}/'.format(bug.id), follow=True)
        self.assertContains(response, "You cannot delete someone bug", 1, 200)

