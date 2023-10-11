from django import forms
from .models import Character


# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Submit, Field

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = "__all__"
