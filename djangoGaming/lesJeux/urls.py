from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('jeu/detail/<str:name>', views.jeu, name='jeu'),
    path('jeu/listejeux', views.listejeux, name='listejeux'),
    path('jeu/creerjeu/', views.creer_jeu, name='creerjeux'),
    path('jeu/modifierjeu/<str:nom>/', views.modifier_jeu, name='modifierjeux'),
    path('jeu/supprimerjeu/<str:nom>/', views.supprimer_jeu, name='supprimerjeux'),
    path('studio/detail/<str:name>', views.studio, name='studio'),
    path('studio/listestudios', views.listestudios, name='listestudios'),
    path('studio/creerstudio/', views.creer_studio, name='creerstudio'),
    path('studio/modifierstudio/<str:nom>/', views.modifier_studio, name='modifierstudio'),
    path('studio/supprimerstudio/<str:nom>/', views.supprimer_studio, name='supprimerstudio'),
    path('tag/detail/<str:name>', views.tag, name='tag'),
    path('tag/listetags', views.listetags, name='listetags'),
    path('tag/creertag/', views.creer_tag, name='creertag'),
    path('tag/modifiertag/<str:nom>/', views.modifier_tag, name='modifiertag'),
    path('tag/supprimertag/<str:nom>/', views.supprimer_tag, name='supprimertag'),
    path('search/', views.search, name='search'),    
]