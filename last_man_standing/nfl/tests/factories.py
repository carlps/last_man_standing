from random import randint

from factory import DjangoModelFactory, Faker, SubFactory

from last_man_standing.nfl.models import (
    NFLTeam,
    NFLDivision,
    NFLConference,
    NFLGame,
    )


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


class NFLGameFactory(DjangoModelFactory):
    class Meta:
        model = NFLGame

    home_team = SubFactory(NFLTeamFactory)
    away_team = SubFactory(NFLTeamFactory)
    season_type = 1
    week = randint(0, 16)
    scheduled_start_time = Faker('date_time')
    home_score = randint(0, 100)
    away_score = randint(0, 100)
