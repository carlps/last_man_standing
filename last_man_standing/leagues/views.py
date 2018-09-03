from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView

from .forms import LeagueCreationForm
from .models import League


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
