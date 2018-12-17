from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    View,
)

from .forms import LeagueCreationForm
from .models import League, LeagueRules


class UserLeagueListView(LoginRequiredMixin, ListView):

    model = League
    template_name = "leagues/user_league_list.html"

    def get_queryset(self):
        user = self.request.user
        leagues_qs = League.objects.get_all_user_leagues(user)
        return leagues_qs


user_league_list_view = UserLeagueListView.as_view()


class LeagueDetailView(LoginRequiredMixin, DetailView):

    model = League
    context_object_name = "league"


league_detail_view = LeagueDetailView.as_view()


class LeagueCreateView(LoginRequiredMixin, CreateView):

    model = League
    form_class = LeagueCreationForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


league_create_view = LeagueCreateView.as_view()


class LeagueRulesUpdateView(LoginRequiredMixin, UpdateView):

    model = LeagueRules
    fields = [
        'max_wrong_picks',
        'max_times_a_team_can_be_picked',
        'latest_pick_accepted_day',
        'latest_pick_accepted_time',
    ]


league_rules_update_view = LeagueRulesUpdateView.as_view()


class LeagueJoinListView(LoginRequiredMixin, ListView):

    model = League
    template_name = "leagues/league_join_list.html"

    def get_queryset(self):
        user = self.request.user
        # only show public leagues user isn't already in
        public_leagues_qs = League.objects.filter(
            is_public=True,
        ).exclude(
            users=user,
        )
        return public_leagues_qs


league_join_list_view = LeagueJoinListView.as_view()


class LeagueJoinView(LoginRequiredMixin, View):
    def get(self, request, league_id, passphrase=None):
        league = League.objects.get(pk=league_id)
        # TODO handle non-public leagues
        if league.passphrase == passphrase:
            league.users.add(request.user)
            return HttpResponseRedirect(reverse('leagues:list'))
        else:
            # TODO
            pass


league_join_view = LeagueJoinView.as_view()
