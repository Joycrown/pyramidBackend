from django import forms
from .models import RegexQuery

class RegexQueryForm(forms.ModelForm):
    class Meta:
        model = RegexQuery
        fields = ['input_string', 'regex_pattern']
