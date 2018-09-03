"""
I want the create form to look like:

League name: _______________
League owner: [user_name]V (dropdown with users, but default to current user)
Public: [x] (checkbox)
Password: _______ (only required if not public
------------
Rules:
Max Wrong Picks: [2]V (dropdown with 1:16)
Max Times a Team can be Picked: [1]V (dropdown with 1:16)
Pick Deadline: [Sunday]V [9:00 AM]V
"""
from django import forms
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from .models import League


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
        return instance
