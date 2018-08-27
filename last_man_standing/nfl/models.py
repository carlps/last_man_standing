from django.db import models


class NFLTeam(models.Model):
    nickname = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=3)
    division = models.ForeignKey(
        'NFLDivision', models.PROTECT, related_name="teams")
    # season = models.IntegerField() # TODO
    wins = models.IntegerField()
    losses = models.IntegerField()
    # status # TODO

    @property
    def fullname(self):
        return f'{self.region} {self.nickname}'

    def __unicode__(self):
        return self.fullname

    def __str__(self):
        return self.__unicode__()

    class Meta:
        ordering = ['region', 'nickname']
        verbose_name = "NFL Team"
        verbose_name_plural = "NFL Teams"


class NFLGame(models.Model):
    home_team = models.ForeignKey(
        NFLTeam, models.PROTECT, related_name="home_games")
    away_team = models.ForeignKey(
        NFLTeam, models.PROTECT, related_name="away_games")
    # TODO what is season_type???
    season_type = models.IntegerField()
    week = models.IntegerField()
    scheduled_start_time = models.DateTimeField()
    home_score = models.IntegerField(default=0)
    away_score = models.IntegerField(default=0)

    def __unicode__(self):
        u = f"{self.home_team} vs {self.away_team} (Week {self.week})"
        return u

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = "NFL Game"
        verbose_name_plural = "NFL Games"


class NFLConference(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=3)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = "NFL Conference"
        verbose_name_plural = "NFL Conferences"


class NFLDivision(models.Model):
    name = models.CharField(max_length=100)
    conference = models.ForeignKey(
        NFLConference, models.PROTECT, related_name="divisions")

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = "NFL Division"
        verbose_name_plural = "NFL Divisions"
