from django import forms
from .models import Jeux
from django.forms import DateInput

class JeuForm(forms.ModelForm):
    class Meta:
        model = Jeux
        fields = ['nom', 'description', 'studio','tags', 'date']
        widgets = {
            'date': DateInput(attrs={'type': 'date'})
        }

