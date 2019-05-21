from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Bugs(models.Model):

    choices = (
        ('todo', 'To do'),
        ('doing', 'Doing'),
        ('done', 'Done')
    )

    name = models.CharField(max_length=256)
    description = models.TextField()
    status = models.CharField(max_length=5, choices=choices, default="todo")
    votes = models.IntegerField(default=0)
    voted_by = models.ManyToManyField(User, related_name='voted_by')
    views = models.IntegerField(default=0)
    author = models.ForeignKey(User, related_name='created_by')

    def __str__(self):
        return self.name


class BugComment(models.Model):
    comment = models.TextField()
    bug = models.ForeignKey(Bugs)
    author = models.ForeignKey(User)

    def __str__(self):
        return self.comment
