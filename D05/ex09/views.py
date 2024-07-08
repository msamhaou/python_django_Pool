from django.shortcuts import render
from .models import People
# Create your views here.

def display(request):
    people = People.objects.all()
    return render(request, "ex09/index.html", {'people' : people})