from django.http import HttpResponse
from django.shortcuts import render
from lesJeux.models import Jeux

def home(request):
  return render(request, template_name='base.html')

def jeu(request, name):
  jeu = Jeux.objects.get(nom=name)
  return render(request, template_name='jeu.html', context={'jeu': jeu})

def listejeux(request):
  jeux = Jeux.objects.all()
  return render(request, template_name='listejeux.html', context={'jeux': jeux})