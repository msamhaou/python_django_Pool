from django import forms

class Delmovie(forms.Form):
    title = forms.CharField(max_length=64)