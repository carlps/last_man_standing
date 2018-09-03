from django.conf import settings
from django.db import models

from last_man_standing.leagues.models import League
from last_man_standing.nfl.models import Season


class Team(models.Model):
    """
    A team that plays in a League and makes Picks.
    Many to Many on Season ensures that a team can exist across multiple
    Seasons.
    """
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, models.PROTECT)
    league = models.ForeignKey(League, models.CASCADE)
    seasons = models.ManyToManyField(Season, through='TeamSeason')


class TeamSeason(models.Model):
    """
    Associate table to join many-to-many Team on Season.
    Maintains season-specific stats for a team. This way,
    Teams can be maintained across seasons and historic data
    remains.
    """
    team = models.ForeignKey(Team, models.CASCADE)
    season = models.ForeignKey(Season, models.PROTECT)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
