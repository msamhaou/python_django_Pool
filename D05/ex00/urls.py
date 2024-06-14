from django.urls import path
from .views import init

urlpatterns = [
    path(route='init/', view=init, name='init')
]