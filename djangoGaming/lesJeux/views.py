from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from lesJeux.models import Jeux
from .forms import JeuForm

def home(request):
  return render(request, template_name='base.html')

def jeu(request, name):
  jeu = Jeux.objects.get(nom=name)
  return render(request, template_name='jeu.html', context={'jeu': jeu})

def listejeux(request):
  jeux = Jeux.objects.all()
  return render(request, template_name='listejeux.html', context={'jeux': jeux})

def creer_jeu(request):
    if request.method == 'POST':
        form = JeuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listejeux')
    else:
        form = JeuForm()
    return render(request, 'creerjeux.html', {'form': form})

def modifier_jeu(request, nom):
    jeu = get_object_or_404(Jeux, nom=nom)
    if request.method == 'POST':
        form = JeuForm(request.POST, instance=jeu)
        if form.is_valid():
            form.save()
            return redirect('listejeux')
    else:
        form = JeuForm(instance=jeu)
    return render(request, 'modifierjeux.html', {'form': form})

def supprimer_jeu(request, nom):
    jeu = get_object_or_404(Jeux, nom=nom)
    jeu.delete()
    return redirect('listejeux')

def studio(request, name):
  studio = Studio.objects.get(nom=name)
  return render(request, template_name='studio.html', context={'studio': studio})

def listestudios(request):
  studios = Studio.objects.all()
  return render(request, template_name='listestudios.html', context={'studios': studios})

def creer_studio(request):
    if request.method == 'POST':
        form = StudioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listestudios')
    else:
        form = StudioForm()
    return render(request, 'creerstudio.html', {'form': form})

def modifier_studio(request, nom):
    studio = get_object_or_404(Studio, nom=nom)
    if request.method == 'POST':
        form = StudioForm(request.POST, instance=studio)
        if form.is_valid():
            form.save()
            return redirect('listestudios')
    else:
        form = StudioForm(instance=jeu)
    return render(request, 'modifierstudios.html', {'form': form})

def supprimer_jeu(request, nom):
    studio = get_object_or_404(Studio, nom=nom)
    studio.delete()
    return redirect('listejeux')