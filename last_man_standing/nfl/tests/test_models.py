import pytest

from last_man_standing.nfl.tests.factories import (
    NFLTeamFactory,
    NFLGameFactory,
    NFLConferenceFactory,
    NFLDivisionFactory,
    )

pytestmark = pytest.mark.django_db


class TestNFLTeam:
    # TODO -- pytest fixtures for shared data
    def test_nfl_team_fullname(self):
        nfl_team = NFLTeamFactory()
        desired_fullname = f"{nfl_team.region} {nfl_team.nickname}"
        assert nfl_team.fullname == desired_fullname

    def test_nfl_team_unicode(self):
        nfl_team = NFLTeamFactory()
        desired_unicode = f"{nfl_team.region} {nfl_team.nickname}"
        assert nfl_team.__unicode__() == desired_unicode

    def test_nfl_team_str(self):
        nfl_team = NFLTeamFactory()
        desired_str = f"{nfl_team.region} {nfl_team.nickname}"
        assert nfl_team.__str__() == desired_str


class TestNFLGame:
    def test_nfl_game_unicode(self):
        nfl_game = NFLGameFactory()
        desired_unicode = "{} vs {} (Week {})".format(
            nfl_game.home_team,
            nfl_game.away_team,
            nfl_game.week
            )
        assert nfl_game.__unicode__() == desired_unicode

    def test_nfl_game_str(self):
        nfl_game = NFLGameFactory()
        desired_str = "{} vs {} (Week {})".format(
            nfl_game.home_team,
            nfl_game.away_team,
            nfl_game.week
            )
        assert nfl_game.__str__() == desired_str


class TestNFLConference:
    def test_nfl_conference_unicode(self):
        nfl_conference = NFLConferenceFactory()
        desired_unicode = nfl_conference.name
        assert nfl_conference.__unicode__() == desired_unicode

    def test_nfl_conference_str(self):
        nfl_conference = NFLConferenceFactory()
        desired_str = nfl_conference.name
        assert nfl_conference.__str__() == desired_str


class TestNFLDivision:
    def test_nfl_division_unicode(self):
        nfl_division = NFLDivisionFactory()
        desired_unicode = nfl_division.name
        assert nfl_division.__unicode__() == desired_unicode

    def test_nfl_division_str(self):
        nfl_division = NFLDivisionFactory()
        desired_str = nfl_division.name
        assert nfl_division.__str__() == desired_str
