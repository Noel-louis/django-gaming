from django.http import HttpResponse
from django.shortcuts import render

def home(request):
  return render(request, template_name='base.html')

def jeu(request, name):
  jeu = {
    'nom': name,
    'description': 'Un jeu de combat',
    'date': '2021-01-01',
    'studio': 'Studio 1',
    'tags': 'Combat, 2D, 3D',
  }
  return render(request, template_name='jeu.html', context={'jeu': jeu})

def listejeux(request):
  jeux = [
    {
      'nom': 'Jeu 1',
      'description': 'Un jeu de combat',
      'date': '2021-01-01',
      'studio': 'Studio 1',
      'tags': 'Combat, 2D, 3D',
    },
    {
      'nom': 'Jeu 2',
      'description': 'Un jeu de combat',
      'date': '2021-01-01',
      'studio': 'Studio 1',
      'tags': 'Combat, 2D, 3D',
    },
    {
      'nom': 'Jeu 3',
      'description': 'Un jeu de combat',
      'date': '2021-01-01',
      'studio': 'Studio 1',
      'tags': 'Combat, 2D, 3D',
    },
    {
      'nom': 'Jeu 4',
      'description': 'Un jeu de combat',
      'date': '2021-01-01',
      'studio': 'Studio 1',
      'tags': 'Combat, 2D, 3D',
    },
    {
      'nom': 'Jeu 5',
      'description': 'Un jeu de combat',
      'date': '2021-01-01',
      'studio': 'Studio 1',
      'tags': 'Combat, 2D, 3D',
    },
    {
      'nom': 'Jeu 6',
      'description': 'Un jeu de combat',
      'date': '2021-01-01',
      'studio': 'Studio 1',
      'tags': 'Combat, 2D, 3D',
    },
  ]
  return render(request, template_name='listejeux.html', context={'jeux': jeux})