from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import localtime
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
    voted_by = models.ManyToManyField(User, blank=True, related_name='voted_by')
    total_votes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    author = models.ForeignKey(User)
    published = models.DateField(default=localtime, editable=False)

    def __str__(self):
        return self.name


class BugComment(models.Model):
    comment = models.TextField()
    bug = models.ForeignKey(Bugs)
    author = models.ForeignKey(User)
    published = models.DateField(default=localtime, editable=False)

    def __str__(self):
        return self.comment
