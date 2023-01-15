from django import forms
from divulge.models.divulge_models import *


class NewPetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ("picture", "name", "description", "province", "city", "tags", "breed")
