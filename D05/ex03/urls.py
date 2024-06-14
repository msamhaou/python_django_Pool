from django.urls import path
from . import views

urlpatterns = [
    path(route='populate/', view=views.Populate),
    path(route='display/', view=views.Display)
]