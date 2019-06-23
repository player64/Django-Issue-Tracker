from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, PostComment


class TestViews(TestCase):

    @staticmethod
    def create_post():
        post = Post(name='Test', description='Test desc')
        post.save()
        return post

    def login(self):
        self.user = User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')

    # ARCHIVE
    def test_archive_page_status(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'archive-blog.html')

    # SINGLE
    def test_single_page_status(self):
        post = self.create_post()
        response = self.client.get('/blog/{}/'.format(post.id))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'single-post.html')

    def test_add_comment_as_not_logged(self):
        post = self.create_post()
        comment = {
            'comment': 'Test comment'
        }
        response = self.client.post('/blog/{}/'.format(post.id), data=comment, follow=True)
        self.assertContains(response, "To add the comment you need to login", 1, 200)

    def test_add_comment(self):
        self.login()
        post = self.create_post()
        comment = {
            'comment': 'Test comment'
        }
        response = self.client.post('/blog/{}/'.format(post.id), data=comment, follow=True)
        self.assertContains(response, "Comment has been added", 1, 200)
        comments = PostComment.objects.filter(post__pk=post.id)
        self.assertEqual(len(comments), 1)
        self.assertEqual(comments[0].comment, 'Test comment')
        self.assertEqual(comments[0].post_id, post.id)
