from django import forms
from .models import Movies

class Delmovie(forms.Form):
    title = forms.CharField(max_length=64)

class PickMovie(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ['opening_crawl']