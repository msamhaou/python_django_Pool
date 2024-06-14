from django.urls import path
from . import views

urlpatterns = [
    path(route='remove/', view=views.Remove, name='remove'),
    path(route='display/', view=views.Display, name='display'),
    path(route='populate/', view=views.Populate, name='populate'),
    path(route='init/', view=views.init, name='init'),
]