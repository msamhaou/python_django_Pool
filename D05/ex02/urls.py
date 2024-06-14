from django.urls import path
from . import views
urlpatterns = [
    path(route='init/', view=views.init),
    path(route='populate/', view=views.Populate)
    # path(round)
]