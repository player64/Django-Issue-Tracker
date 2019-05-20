# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-20 21:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BugComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bugs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('todo', 'To do'), ('doing', 'Doing'), ('done', 'Done')], default='todo', max_length=5)),
                ('votes', models.IntegerField(default=0)),
                ('views', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='bugcomment',
            name='bug',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bugs.Bugs'),
        ),
    ]
