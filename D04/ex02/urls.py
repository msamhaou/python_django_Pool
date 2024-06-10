from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.get_name, name='form'),
]