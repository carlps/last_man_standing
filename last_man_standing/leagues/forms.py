from django import forms
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from ..nfl.models import Season
from .models import League, LeagueRules


class LeagueCreationForm(forms.ModelForm):

    class Meta:
        model = League
        fields = ['name', 'is_public', 'passphrase']
        widgets = {
            'is_public': forms.RadioSelect(),
            }
        labels = {
            'is_public': 'League Privacy',
            }
        help_texts = {
            'is_public': _("Public leagues will be listed and accessible by anyone."),
            'passphrase': _("Optional for public leagues, required for private leagues."),
            }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['passphrase'].required = False

    def clean(self):
        cleaned_data = super().clean()
        is_public = cleaned_data.get("is_public")
        passphrase = cleaned_data.get("passphrase")
        if not is_public and not passphrase:
            error = forms.ValidationError(
                "Passphrase is required for private leagues."
                )
            self.add_error("passphrase", error)

    def save(self):
        # Generate a slug on form save
        instance = super().save(commit=False)
        instance.slug = slugify(instance.name)
        instance.save()
        # generate a default ruleset for new league
        season = Season.objects.get(is_active=True)
        rules = LeagueRules.objects.create(
            league=instance,
            season=season)
        rules.save()

        return instance
