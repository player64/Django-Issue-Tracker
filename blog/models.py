from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import localtime
# Create your models here.


class Post(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    published = models.DateField(default=localtime, editable=False)

    def __str__(self):
        return self.name


class PostComment(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(Post)
    author = models.ForeignKey(User)
    published = models.DateField(default=localtime, editable=False)

    def __str__(self):
        return self.comment
