# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-23 09:44
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Batsman',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Bowler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counter', models.IntegerField(default=0)),
                ('total', models.IntegerField(default=1)),
                ('arr', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True), size=None)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserSelect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(blank=True, choices=[('1', 'Team A'), ('2', 'Team B'), ('3', 'Team C'), ('4', 'Team D'), ('5', 'Team E')], default='1', max_length=1)),
                ('batsman', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='batsman', to='main.Batsman')),
                ('bowler', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bowlers', to='main.Bowler')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='bowler',
            name='users',
            field=models.ManyToManyField(through='main.UserSelect', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='batsman',
            name='users',
            field=models.ManyToManyField(through='main.UserSelect', to=settings.AUTH_USER_MODEL),
        ),
    ]
