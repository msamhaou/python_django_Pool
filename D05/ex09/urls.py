from django.urls import path
from . import views

urlpatterns = [
    path(route='display', view=views.display, name='display'),
]