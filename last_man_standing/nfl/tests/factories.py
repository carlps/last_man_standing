import datetime
from random import randint

from factory import DjangoModelFactory, Faker, SubFactory

from last_man_standing.nfl.models import (
    NFLTeam,
    NFLDivision,
    NFLConference,
    NFLGame,
    Season,
    Week,
    )


class SeasonFactory(DjangoModelFactory):
    class Meta:
        model = Season

    year = 2018
    season_start_date = datetime.date(year=2018, month=9, day=6)
    season_end_date = datetime.date(year=2018, month=12, day=30)
    is_active = True


class WeekFactory(DjangoModelFactory):
    class Meta:
        model = Week

    week_number = 1
    season = SubFactory(SeasonFactory)


class NFLConferenceFactory(DjangoModelFactory):
    class Meta:
        model = NFLConference

    name = "International Football Conference"
    abbreviation = "IFC"


class NFLDivisionFactory(DjangoModelFactory):
    class Meta:
        model = NFLDivision

    name = "IFC West"
    conference = SubFactory(NFLConferenceFactory)


class NFLTeamFactory(DjangoModelFactory):
    class Meta:
        model = NFLTeam

    nickname = 'Dukes'
    region = 'Albuquerque'
    abbreviation = 'ABQ'
    division = SubFactory(NFLDivisionFactory)
    # TODO -- fake wins/losses based on week?
    wins = randint(0, 16)
    losses = randint(0, 16)
    season = SubFactory(SeasonFactory)
    is_active = True


class NFLGameFactory(DjangoModelFactory):
    class Meta:
        model = NFLGame

    home_team = SubFactory(NFLTeamFactory)
    away_team = SubFactory(NFLTeamFactory)
    week = SubFactory(WeekFactory)
    scheduled_start_time = Faker('date_time')
    home_score = randint(0, 100)
    away_score = randint(0, 100)
