from django.db import models

from last_man_standing.nfl.models import NFLGame, NFLTeam, Season
from last_man_standing.teams.models import Team


class Pick(models.Model):
    """
    A Team makes a Pick of a NFLTeam to win a NFLGame.
    Picks are controlled by LeagueRules for the League
    that the Team is in. One Pick is made for one Season.
    """
    team = models.ForeignKey(Team, models.CASCADE)
    season = models.ForeignKey(Season, models.PROTECT)
    week = models.IntegerField()
    game = models.ForeignKey(NFLGame, models.PROTECT)
    picked_team = models.ForeignKey(NFLTeam, models.PROTECT)
