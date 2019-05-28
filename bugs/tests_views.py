from django.test import TestCase
from django.contrib.auth.models import User
from .models import Bugs, BugComment


class TestViews(TestCase):

    @staticmethod
    def create_other_user():
        return User.objects.create_user(username='other_user', password='password')

    @staticmethod
    def create_bug(user):
        bug = Bugs(name='Test', description='Test desc', author=user)
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

    def test_single_views(self):
        bug = self.create_bug(self.create_other_user())
        self.client.get('/bugs/{}/'.format(bug.id))
        bug.refresh_from_db()
        self.assertEqual(bug.views, 1)
        # test is the session working correctly
        self.client.get('/bugs/{}/'.format(bug.id))
        bug.refresh_from_db()
        self.assertEqual(bug.views, 1)

    def test_views_own_bug(self):
        bug = self.create_bug(self.user)
        self.client.get('/bugs/{}/'.format(bug.id))
        bug.refresh_from_db()
        self.assertEqual(bug.views, 0)

    def test_add_new_comment(self):
        bug = self.create_bug(self.user)
        comment = {
            'comment': 'Test comment'
        }
        response = self.client.post('/bugs/{}/'.format(bug.id), data=comment,
                                    follow=True)
        self.assertContains(response, "Comment has been added", 1, 200)
        comments = BugComment.objects.filter(bug__pk=bug.id)
        self.assertEqual(len(comments), 1)
        self.assertEqual(comments[0].comment, 'Test comment')
        self.assertEqual(comments[0].bug_id, bug.id)

    # ADD
    def test_add_status(self):
        response = self.client.get('/bugs/new/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_edit.html')

    def test_add_new_bug(self):
        new_bug = {
            'name': 'Bug Test',
            'description': 'Bug description'
        }
        response = self.client.post('/bugs/new/', data=new_bug, follow=True)
        self.assertContains(response, "Bug has been created", 1, 200)
        self.assertTemplateUsed(response, 'single.html')

    # EDIT
    def test_edit_status(self):
        bug = self.create_bug(self.user)
        response = self.client.get('/bugs/edit/{}/'.format(bug.id))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_edit.html')

    def test_edit_bug(self):
        bug = self.create_bug(self.user)
        edit_data = {
            'name': 'New bug name',
            'description': 'New description'
        }
        response = self.client.post('/bugs/edit/{}/'.format(bug.id), data=edit_data, follow=True)
        edited_bug = Bugs.objects.get(id=bug.id)
        self.assertEqual(edited_bug.name, edit_data['name'])
        self.assertEqual(edited_bug.description, edit_data['description'])
        self.assertEqual(edited_bug.status, 'todo')
        self.assertEqual(edited_bug.views, 0)
        self.assertEqual(edited_bug.author_id, self.user.id)
        self.assertContains(response, "Bug has been edited", 1, 200)
        self.assertTemplateUsed(response, 'single.html')

    def test_edit_someone_bug_by_get(self):
        bug = self.create_bug(self.create_other_user())
        response = self.client.post('/bugs/edit/{}/'.format(bug.id), follow=True)
        self.assertContains(response, "You cannot edit someone bug", 1, 200)

    def test_edit_someone_bug_by_post(self):
        bug = self.create_bug(self.create_other_user())
        response = self.client.post('/bugs/edit/{}/'.format(bug.id), follow=True)
        self.assertContains(response, "You cannot edit someone bug", 1, 200)

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

    def test_vote_on_own_bug(self):
        bug = self.create_bug(self.user)
        response = self.client.post('/bugs/vote/{}/'.format(bug.id), follow=True)
        bug.refresh_from_db()
        self.assertEqual(len(bug.voted_by.values_list()), 0)
        self.assertContains(response, "You cannot vote for own bug", 1, 200)

    def test_vote_and_check_redirection_when_next_get_is_defined(self):
        bug = self.create_bug(self.create_other_user())
        response = self.client.post('/bugs/vote/{0}/?next=/bugs/{0}/'.format(bug.id), follow=True)
        self.assertContains(response, "You have voted up for this bug", 1, 200)
        self.assertTemplateUsed(response, 'single.html')

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
