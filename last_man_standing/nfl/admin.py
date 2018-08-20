from django.contrib import admin

from .models import NFLTeam, NFLGame, NFLConference, NFLDivision

admin.site.register(NFLTeam)
admin.site.register(NFLGame)
admin.site.register(NFLConference)
admin.site.register(NFLDivision)
