# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-23 19:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0003_auto_20190521_2344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bugs',
            name='votes',
        ),
        migrations.AlterField(
            model_name='bugs',
            name='voted_by',
            field=models.ManyToManyField(blank=True, related_name='voted_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
