# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-24 10:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='features',
            name='paid_by',
            field=models.IntegerField(default=0),
        ),
    ]
