from django import forms
from .models import Character
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(CharacterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('name'),
            Field('text'),
            Field('image'),
            Submit('submit', 'Submit', css_class='btn btn-dark')
        )
