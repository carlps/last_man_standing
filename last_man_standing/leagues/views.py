from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView

from .forms import LeagueCreationForm
from .models import League


class LeagueListView(LoginRequiredMixin, ListView):

    model = League

    def get_queryset(self):
        user = self.request.user
        leagues_qs = League.objects.get_all_user_leagues(user)
        return leagues_qs

league_list_view = LeagueListView.as_view()


class LeagueDetailView(LoginRequiredMixin, DetailView):

    model = League


league_detail_view = LeagueDetailView.as_view()


class LeagueCreateView(LoginRequiredMixin, CreateView):

    model = League
    form_class = LeagueCreationForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


league_create_view = LeagueCreateView.as_view()
