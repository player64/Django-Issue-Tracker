from django.test import TestCase
from django.contrib.auth.models import User
from .models import Features, FeatureComment


class TestViews(TestCase):
    @staticmethod
    def create_other_user():
        return User.objects.create_user(username='other_user', password='password')

    @staticmethod
    def create_feature(user):
        feature = Features(name='Test', description='Test desc', author=user)
        feature.save()
        return feature

    def setUp(self):
        self.user = User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')

    # ARCHIVE
    def test_archive_page_status(self):
        response = self.client.get('/features/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'archive.html')

    # SINGLE
    def test_single_page_status(self):
        user = self.create_other_user()
        feature = self.create_feature(user)
        response = self.client.get('/features/{}/'.format(feature.id))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'single.html')

    def test_single_views(self):
        feature = self.create_feature(self.create_other_user())
        self.client.get('/features/{}/'.format(feature.id))
        feature.refresh_from_db()
        self.assertEqual(feature.views, 1)
        # test is the session working correctly
        self.client.get('/features/{}/'.format(feature.id))
        feature.refresh_from_db()
        self.assertEqual(feature.views, 1)

    def test_views_own_feature(self):
        feature = self.create_feature(self.user)
        self.client.get('/features/{}/'.format(feature.id))
        feature.refresh_from_db()
        self.assertEqual(feature.views, 0)

    def test_add_new_comment(self):
        feature = self.create_feature(self.user)
        comment = {
            'comment': 'Test comment'
        }
        response = self.client.post('/features/{}/'.format(feature.id), data=comment,
                                    follow=True)
        self.assertContains(response, "Comment has been added", 1, 200)
        comments = FeatureComment.objects.filter(feature__pk=feature.id)
        self.assertEqual(len(comments), 1)
        self.assertEqual(comments[0].comment, 'Test comment')
        self.assertEqual(comments[0].feature_id, feature.id)

    # ADD
    def test_add_status(self):
        response = self.client.get('/features/new/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add.html')

    def test_add_new_feature(self):
        new_feature = {
            'name': 'Feature Test',
            'description': 'Feature description'
        }
        response = self.client.post('/features/new/', data=new_feature, follow=True)
        self.assertContains(response, "Feature has been created", 1, 200)
        self.assertTemplateUsed(response, 'single.html')

    # EDIT
    def test_edit_status(self):
        feature = self.create_feature(self.user)
        response = self.client.get('/features/edit/{}/'.format(feature.id))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit.html')

    def test_edit_feature(self):
        feature = self.create_feature(self.user)
        edit_data = {
            'name': 'New feature name',
            'description': 'New description'
        }
        response = self.client.post('/features/edit/{}/'.format(feature.id),
                                    data=edit_data, follow=True)
        edited_feature = Features.objects.get(id=feature.id)
        self.assertEqual(edited_feature.name, edit_data['name'])
        self.assertEqual(edited_feature.description, edit_data['description'])
        self.assertEqual(edited_feature.status, 'todo')
        self.assertEqual(edited_feature.views, 0)
        self.assertEqual(edited_feature.author_id, self.user.id)
        self.assertContains(response, "Feature has been edited", 1, 200)
        self.assertTemplateUsed(response, 'single.html')

    def test_edit_someone_feature_by_get(self):
        feature = self.create_feature(self.create_other_user())
        response = self.client.post('/features/edit/{}/'.format(feature.id), follow=True)
        self.assertContains(response, "You cannot edit someone feature", 1, 200)

    def test_edit_someone_bug_by_post(self):
        feature = self.create_feature(self.create_other_user())
        response = self.client.post('/features/edit/{}/'.format(feature.id), follow=True)
        self.assertContains(response, "You cannot edit someone feature", 1, 200)

    # DELETE
    def test_delete_bug(self):
        feature = self.create_feature(self.user)
        self.client.post('/features/delete/{}/'.format(feature.id), follow=True)
        count_bugs = Features.objects.count()
        self.assertEqual(count_bugs, 0)

    def test_delete_someone_bug(self):
        user = self.create_other_user()
        feature = self.create_feature(user)
        response = self.client.post('/features/delete/{}/'.format(feature.id), follow=True)
        self.assertContains(response, "You cannot delete someone feature", 1, 200)
