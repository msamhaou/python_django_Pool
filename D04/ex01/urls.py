from django.urls import path
from . import views

urlpatterns = [
    path(route='', view=views.base, name='base'),
    path(route='django/', view=views.djan, name='django'),
    path(route='display/', view=views.display, name='display'),
    path(route='templates/', view=views.templates, name='templates'),
    
]