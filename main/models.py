from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from player import *
from player.models import *


class Team(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    counter = models.IntegerField(default=0)
    total = models.IntegerField(default=1)
    arr = ArrayField(models.IntegerField(blank=True))

    def __str__(self):
        return '{0}, {1}'.format(self.user, self.total, self.arr)


class UserSelect(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bowler = models.ForeignKey(Bowlers, on_delete=models.CASCADE, related_name='bowlers', null=True, blank=True)
    batsman = models.ForeignKey(Batsmen, on_delete=models.CASCADE, related_name='batsman', null=True, blank=True)
    TEAM_STATUS = (
        ('1', 'Team A'),
        ('2', 'Team B'),
        ('3', 'Team C'),
        ('4', 'Team D'),
        ('5', 'Team E'),
    )
    team = models.CharField(max_length=1, choices=TEAM_STATUS, blank=True, default='1')

    def __str__(self):
        return '{0}, {1}'.format(self.user, self.team)

