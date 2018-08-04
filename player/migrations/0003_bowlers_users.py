# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-26 10:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_auto_20180726_1523'),
        ('player', '0002_auto_20180726_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='bowlers',
            name='users',
            field=models.ManyToManyField(through='main.UserSelect', to=settings.AUTH_USER_MODEL),
        ),
    ]