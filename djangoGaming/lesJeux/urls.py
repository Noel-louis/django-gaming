from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('jeu/<str:name>', views.jeu, name='jeu'),
    path('listejeux', views.listejeux, name='listejeux'),
    path('creer/', views.creer_jeu, name='creerjeux'),
    path('modifier/<str:nom>/', views.modifier_jeu, name='modifierjeux'),
    path('supprimer/<str:nom>/', views.supprimer_jeu, name='supprimerjeux'),
    path('studio/<str:name>', views.studio, name='studio'),
    path('listestudios', views.listestudios, name='listestudios'),
    path('creerstudio/', views.creer_studio, name='creerstudio'),
    path('modifierstudio/<str:nom>/', views.modifier_studio, name='modifierstudio'),
    path('supprimerstudio/<str:nom>/', views.supprimer_studio, name='supprimerstudio'),
]