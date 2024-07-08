from django import forms

class Delmovie(forms.Form):
    title = forms.CharField(max_length=64)
    
class  OpeningForm(forms.Form):
    title = forms.CharField(max_length=64)
    opening_crawl = forms.TextInput()