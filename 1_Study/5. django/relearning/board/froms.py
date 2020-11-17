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

class RawResisterForm(forms.Form):
    name = forms.CharField(max_length=20)
    date = forms.TimeField(widget=forms.TextInput(attrs={"placeholder":"YYYY-MM-DD"}))
    etc = forms.CharField(widget=forms.Textarea(attrs={"class":"whatever","rows":3,"cols":120}))