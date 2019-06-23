import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'issue_tracker.settings')
import django

django.setup()
from bugs.models import Bugs, BugComment
from features.models import Features, FeatureComment
from blog.models import Post, PostComment
from django.contrib.auth.models import User
from faker import Faker
import random

obj = Faker('en_GB')


def get_random_user():
    users = User.objects.all()
    return random.choice(users)


def create_users(no):
    for i in range(no):
        User.objects.create_user(username=obj.first_name(),
                                 email=obj.email(),
                                 password=obj.password())


def convert_list_to_string(sentence):
    out = ''
    for item in sentence:
        out += item
    return out


statuses = ['todo', 'doing', 'done']


def create_bugs(no):
    for i in range(no):
        votes = obj.random_int(min=0, max=87)
        Bugs.objects.get_or_create(name=convert_list_to_string(obj.text(max_nb_chars=30)),
                                   description=convert_list_to_string(obj.paragraphs(nb=5)),
                                   status=random.choice(statuses),
                                   total_votes=votes,
                                   views=obj.random_int(min=votes, max=300),
                                   author=get_random_user(),
                                   published=obj.date_time_between(start_date='-1y', end_date='now'))


def create_features(no):
    for i in range(no):
        votes = obj.random_int(min=0, max=87)
        Features.objects.get_or_create(name=convert_list_to_string(obj.text(max_nb_chars=30)),
                                       description=convert_list_to_string(obj.paragraphs(nb=5)),
                                       status=random.choice(statuses),
                                       total_votes=votes,
                                       views=obj.random_int(min=votes, max=300),
                                       author=get_random_user(),
                                       published=obj.date_time_between(start_date='-1y',
                                                                       end_date='now'))


def get_random_post(post_type):
    if post_type == 'bugs':
        return random.choice(Bugs.objects.all())
    elif post_type == 'feature':
        return random.choice(Features.objects.all())
    elif post_type == 'blog':
        return random.choice(Post.objects.all())


def create_bugs_comments(no):
    for i in range(no):
        BugComment.objects.get_or_create(comment=convert_list_to_string(obj.paragraphs(nb=5)),
                                         bug_id=get_random_post('bug').id,
                                         author=get_random_user(),
                                         published=obj.date_time_between(start_date='-1y',
                                                                         end_date='now'))


def create_features_comments(no):
    for i in range(no):
        FeatureComment.objects.get_or_create(comment=convert_list_to_string(obj.paragraphs(nb=5)),
                                             feature_id=get_random_post('feature').id,
                                             author=get_random_user(),
                                             published=obj.date_time_between(start_date='-1y',
                                                                             end_date='now'))


def create_blog_posts(no):
    for i in range(no):
        Post.objects.get_or_create(name=convert_list_to_string(obj.text(max_nb_chars=30)),
                                   description=convert_list_to_string(obj.paragraphs(nb=5)),
                                   published=obj.date_time_between(start_date='-1y', end_date='now'))


def create_blog_post_comment(no):
    for i in range(no):
        PostComment.objects.get_or_create(comment=convert_list_to_string(obj.paragraphs(nb=5)),
                                          post_id=get_random_post('blog').id,
                                          author=get_random_user(),
                                          published=obj.date_time_between(start_date='-1y',
                                                                          end_date='now'))


if __name__ == '__main__':
    print("Filling random data")
    # create_users(30)
    # create_bugs(40)
    # create_features(40)
    # create_bugs_comments(60)
    # create_features_comments(60)
    create_blog_posts(40)
    create_blog_post_comment(60)
    print("Filling done ")
