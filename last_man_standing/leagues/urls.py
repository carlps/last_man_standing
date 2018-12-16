from django.urls import path

from last_man_standing.leagues.views import (
    league_create_view,
    league_detail_view,
    league_list_view,
    league_rules_update_view,
    )

app_name = "leagues"
urlpatterns = [
    path("~create/", view=league_create_view, name="create"),
    path("<str:slug>/", view=league_detail_view, name="detail"),
    path("", view=league_list_view, name="list"),
    path("rules/<int:pk>/", view=league_rules_update_view, name="rules_update")
]
