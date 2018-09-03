from django.contrib import admin

from .models import (
    NFLTeam,
    NFLGame,
    NFLConference,
    NFLDivision,
    Season,
    Week,
    )

admin.site.register(Season)
admin.site.register(Week)
admin.site.register(NFLTeam)
admin.site.register(NFLGame)
admin.site.register(NFLConference)
admin.site.register(NFLDivision)
