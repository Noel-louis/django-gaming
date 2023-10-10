from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('jeu/<str:name>', views.jeu, name='jeu'),
    path('listejeux', views.listejeux, name='listejeux'),
]