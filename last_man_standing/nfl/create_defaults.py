from datetime import date

from last_man_standing.nfl.models import Season, NFLConference, NFLDivision, NFLTeam


def create_2018_season():
    season = Season.objects.create(
        year=2018,
        season_start_date=date(year=2018, month=9, day=6),
        season_end_date=date(year=2018, month=12, day=30),
        )
    return season


def create_2018_weeks():
    # TODO
    pass


def create_afc_and_nfc():
    afc = NFLConference.objects.create(
        name='American Football Conference',
        abbreviation='AFC',
        )
    nfc = NFLConference.objects.create(
        name='National Football Conference',
        abbreviation='NFC',
        )


def create_default_divisions():
    afc = NFLConference.objects.get(abbreviation='AFC')
    nfc = NFLConference.objects.get(abbreviation='NFC')

    afc_east = NFLDivision.objects.create(
        name='AFC East',
        conference=afc,
        )
    afc_west = NFLDivision.objects.create(
        name='AFC West',
        conference=afc,
        )
    afc_north = NFLDivision.objects.create(
        name='AFC North',
        conference=afc,
        )
    afc_south = NFLDivision.objects.create(
        name='AFC South',
        conference=afc,
        )
    nfc_east = NFLDivision.objects.create(
        name='NFC East',
        conference=nfc,
        )
    nfc_west = NFLDivision.objects.create(
        name='NFC West',
        conference=nfc,
        )
    nfc_north = NFLDivision.objects.create(
        name='NFC North',
        conference=nfc,
        )
    nfc_south = NFLDivision.objects.create(
        name='NFC South',
        conference=nfc,
        )

def create_default_teams():
    afc_east = NFLDivision.objects.get(name="AFC East")
    afc_west = NFLDivision.objects.get(name="AFC West")
    afc_north = NFLDivision.objects.get(name="AFC North")
    afc_south = NFLDivision.objects.get(name="AFC South")
    nfc_east = NFLDivision.objects.get(name="NFC East")
    nfc_west = NFLDivision.objects.get(name="NFC West")
    nfc_north = NFLDivision.objects.get(name="NFC North")
    nfc_south = NFLDivision.objects.get(name="NFC South")

    season = Season.objects.get(year=2018)

    cardinals = NFLTeam.objects.create(
        nickname='Cardinals',
        region='Arizona',
        abbreviation='ARI',
        division=nfc_west,
        wins=0,
        losses=0,
        season=season,
        is_active=True,
        )
    falcons = NFLTeam.objects.create(
        nickname='Falcons',
        region='Atlanta',
        abbreviation='ATL',
        division=nfc_south,
        wins=0,
        losses=0,
        season=season,
        is_active=True,
        )
    ravens = NFLTeam.objects.create(
        nickname='Ravens',
        region='Baltimore',
        abbreviation='BAL',
        division=afc_north,
        wins=0,
        losses=0,
        season=season,
        is_active=True,
        )
    bills = NFLTeam.objects.create(
        nickname='Bills',
        region='Buffalo',
        abbreviation='BUF',
        division=afc_east,
        wins=0,
        losses=0,
        season=season,
        is_active=True,
        )
    panthers = NFLTeam.objects.create(
        nickname='Panthers',
        region='Carolina',
        abbreviation='CAR',
        division=nfc_south,
        wins=0,
        losses=0,
        season=season,
        is_active=True,
        )
    bears = NFLTeam.objects.create(
        nickname='Bears',
        region='Chicago',
        abbreviation='CHI',
        division=nfc_north,
        wins=0,
        losses=0,
        season=season,
        is_active=True,
        )
    bengals = NFLTeam.objects.create(
        nickname='Bengals',
        region='Cincinatti',
        abbreviation='CIN',
        division=afc_north,
        wins=0,
        losses=0,
        season=season,
        is_active=True,
        )
    browns = NFLTeam.objects.create(
        nickname='Browns',
        region='Cleveland',
        abbreviation='CLE',
        division=afc_north,
        wins=0,
        losses=0,
        season=season,
        is_active=True,
        )
    cowboys = NFLTeam.objects.create(
        nickname='Cowboys',
        region='Dallas',
        abbreviation='DAL',
        division=nfc_east,
        wins=0,
        losses=0,
        season=season,
        is_active=True,
        )
    broncos = NFLTeam.objects.create(
        nickname='Broncos',
        region='Denver',
        abbreviation='DEN',
        division=afc_west,
        wins=0,
        losses=0,
        season=season,
        is_active=True,
        )
    lions = NFLTeam.objects.create(
        nickname='Lions',
        region='Detroit',
        abbreviation='DET',
        division=nfc_north,
        wins=0,
        losses=0,
        season=season,
        is_active=True,
        )
    packers = NFLTeam.objects.create(
        nickname='Packers',
        region='Green Bay',
        abbreviation='GB',
        division=nfc_north,
        wins=0,
        losses=0,
        season=season,
        is_active=True,
        )
    texans = NFLTeam.objects.create(
        nickname='Texans',
        region='Houston',
        abbreviation='HOU',
        division=afc_south,
        wins=0,
        losses=0,
        season=season,
        is_active=True,
        )
    colts = NFLTeam.objects.create(
        nickname='Colts',
        region='Indianapolis',
        abbreviation='IND',
        division=afc_south,
        wins=0,
        losses=0,
        season=season,
        is_active=True,
        )
    jaguars = NFLTeam.objects.create(
        nickname='Jaguars',
        region='Jacksonville',
        abbreviation='JAX',
        division=afc_south,
        wins=0,
        losses=0,
        season=season,
        is_active=True,
        )
    chiefs = NFLTeam.objects.create(
        nickname='Chiefs',
        region='Kansas City',
        abbreviation='KC',
        division=afc_west,
        wins=0,
        losses=0,
        season=season,
        is_active=True,
        )
    chargers = NFLTeam.objects.create(
        nickname='Chargers',
        region='Los Angeles',
        abbreviation='LAC',
        division=afc_west,
        wins=0,
        losses=0,
        season=season,
        is_active=True,
        )
    rams = NFLTeam.objects.create(
        nickname='Rams',
        region='Los Angeles',
        abbreviation='LA',
        division=nfc_west,
        wins=0,
        losses=0,
        season=season,
        is_active=True,
        )
    dolphins = NFLTeam.objects.create(
        nickname='Dolphins',
        region='Miami',
        abbreviation='MIA',
        division=afc_east,
        wins=0,
        losses=0,
        season=season,
        is_active=True,
        )
    vikings = NFLTeam.objects.create(
        nickname='Vikings',
        region='Minnesota',
        abbreviation='MIN',
        division=nfc_north,
        wins=0,
        losses=0,
        season=season,
        is_active=True,
        )
    patriots = NFLTeam.objects.create(
        nickname='Patriots',
        region='New England',
        abbreviation='NE',
        division=afc_east,
        wins=0,
        losses=0,
        season=season,
        is_active=True,
        )
    saints = NFLTeam.objects.create(
        nickname='Saints',
        region='New Orleans',
        abbreviation='NO',
        division=nfc_south,
        wins=0,
        losses=0,
        season=season,
        is_active=True,
        )
    giants = NFLTeam.objects.create(
        nickname='Giants',
        region='New York',
        abbreviation='NYG',
        division=nfc_east,
        wins=0,
        losses=0,
        season=season,
        is_active=True,
        )
    jets = NFLTeam.objects.create(
        nickname='Jets',
        region='New York',
        abbreviation='NYJ',
        division=afc_east,
        wins=0,
        losses=0,
        season=season,
        is_active=True,
        )
    raiders = NFLTeam.objects.create(
        nickname='Raiders',
        region='Oakland',
        abbreviation='OAK',
        division=afc_west,
        wins=0,
        losses=0,
        season=season,
        is_active=True,
        )
    eagles = NFLTeam.objects.create(
        nickname='Eagles',
        region='Philadelphia',
        abbreviation='PHI',
        division=nfc_east,
        wins=0,
        losses=0,
        season=season,
        is_active=True,
        )
    steelers = NFLTeam.objects.create(
        nickname='Steelers',
        region='Pittsburgh',
        abbreviation='PIT',
        division=afc_north,
        wins=0,
        losses=0,
        season=season,
        is_active=True,
        )
    fortyniners = NFLTeam.objects.create(
        nickname='49ers',
        region='San Francisco',
        abbreviation='SF',
        division=nfc_west,
        wins=0,
        losses=0,
        season=season,
        is_active=True,
        )
    seahawks = NFLTeam.objects.create(
        nickname='Seahawks',
        region='Seattle',
        abbreviation='SEA',
        division=nfc_west,
        wins=0,
        losses=0,
        season=season,
        is_active=True,
        )
    buccaneers = NFLTeam.objects.create(
        nickname='Buccaneers',
        region='Tampa Bay',
        abbreviation='TB',
        division=nfc_south,
        wins=0,
        losses=0,
        season=season,
        is_active=True,
        )
    titans = NFLTeam.objects.create(
        nickname='Titans',
        region='Tennessee',
        abbreviation='TEN',
        division=afc_south,
        wins=0,
        losses=0,
        season=season,
        is_active=True,
        )
    redskins = NFLTeam.objects.create(
        nickname='Redskins',
        region='Washington',
        abbreviation='WAS',
        division=nfc_east,
        wins=0,
        losses=0,
        season=season,
        is_active=True,
        )


def main():
    create_2018_season()
    create_2018_weeks()
    create_afc_and_nfc()
    create_default_divisions()
    create_default_teams()
