# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-23 19:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0004_auto_20190523_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugs',
            name='voted_by',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
