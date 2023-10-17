from django import forms
from .models import Jeux, Studio, Tag
from django.forms import DateInput

class JeuForm(forms.ModelForm):
    class Meta:
        model = Jeux
        fields = ['nom', 'description', 'studio','tags', 'date']
        widgets = {
            'date': DateInput(attrs={'type': 'date'})
        }

class StudioForm(forms.ModelForm):
    class Meta:
        model = Studio
        fields = ['nom', 'description', 'date_creation']
        widgets = {
            'date_creation': DateInput(attrs={'type': 'date'})
        }

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['nom', 'description']
