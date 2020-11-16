from django import forms
from .models import register

class resisterForm(forms.ModelForm):
    class Meta:
        model = register
        fields = [
            'name',
            'date',
            'etc'
        ]
