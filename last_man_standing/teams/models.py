from django.conf import settings
from django.db import models

from last_man_standing.leagues.models import League


class Team(models.Model):
    """
    A team that plays in a League and makes Picks.
    """
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, models.PROTECT)
    league = models.ForeignKey(League, models.CASCADE)
