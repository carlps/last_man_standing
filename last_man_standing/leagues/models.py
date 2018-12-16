from datetime import time

from django.conf import settings
from django.db import models
from django.urls import reverse

from last_man_standing.nfl.models import Season


class LeagueManager(models.Manager):

    def get_all_user_leagues(self, user):
        """
        Returns all leagues a user owns or has team(s) in.
        """
        return self.filter(models.Q(owner=user) |
                           models.Q(team__owner=user))


class League(models.Model):
    """
    Represents a league playing a season of last man standing.
    Made up of teams, rules and an owner.
    """
    name = models.CharField(max_length=100, unique=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, models.PROTECT)
    IS_PUBLIC_CHOICES = ((True, "Public"), (False, "Private"))
    is_public = models.BooleanField(
        default=True, choices=IS_PUBLIC_CHOICES)
    # passphrase is only needed if is_public==False
    passphrase = models.CharField(null=True, max_length=100, default=None)
    slug = models.SlugField(max_length=100, unique=True)

    objects = LeagueManager()

    def get_absolute_url(self):
        return reverse("leagues:detail", kwargs={"slug": self.slug})


class LeagueRules(models.Model):
    """
    Each field is an actionable rule for league. Set once at
    the beginning of the season and can't be changed after.
    """
    # Eventually we will probably want to keep track of historical rules
    # but for now it will just be OneToOne
    league = models.OneToOneField(League, models.CASCADE, related_name="rules")
    season = models.ForeignKey(Season, models.PROTECT)
    max_wrong_picks = models.IntegerField(default=2)
    max_times_a_team_can_be_picked = models.SmallIntegerField(default=2)

    # Last pick accepted is at a day and time, probably Sunday morning.
    # Need validation in here to ensure no weird stuff is set.

    ACCEPTED_DAY_CHOICES = (
        (0, 'Friday'),
        (1, 'Saturday'),
        (2, 'Sunday'),
        )
    latest_pick_accepted_day = models.SmallIntegerField(
        default=2,
        choices=ACCEPTED_DAY_CHOICES)

    # TODO: Timezone?
    latest_pick_accepted_time = models.TimeField(default=time(hour=9))

    def get_absolute_url(self):
        # rules should be shown with league detail (for now)
        return reverse('leagues:detail', kwargs={'slug': self.league.slug})
