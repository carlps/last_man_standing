from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy

from .forms import LeagueCreationForm
from .models import League, LeagueRules


class LeagueListView(LoginRequiredMixin, ListView):

    model = League

    def get_queryset(self):
        user = self.request.user
        leagues_qs = League.objects.get_all_user_leagues(user)
        return leagues_qs


league_list_view = LeagueListView.as_view()


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
    # TODO -- redirect to detail slug=rules.league
    #success_url = reverse_lazy('detail', kwargs={})


league_rules_update_view = LeagueRulesUpdateView.as_view()
