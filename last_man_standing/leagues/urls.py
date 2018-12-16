from django.urls import path

from last_man_standing.leagues.views import (
    league_create_view,
    league_detail_view,
    league_join_list_view,
    league_join_view,
    league_rules_update_view,
    user_league_list_view,
    )

app_name = "leagues"
urlpatterns = [
    path("~create/", view=league_create_view, name="create"),
    path("<str:slug>/", view=league_detail_view, name="detail"),
    path("", view=user_league_list_view, name="list"),
    path("rules/<int:pk>/", view=league_rules_update_view, name="rules_update"),
    path("join", view=league_join_list_view, name="join"),
    path("join/<int:league_id>", view=league_join_view, name="join_league"),
]
