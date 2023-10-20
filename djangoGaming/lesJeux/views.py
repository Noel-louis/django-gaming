from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from lesJeux.models import Jeux, Studio, Tag
from .forms import JeuForm, StudioForm, TagForm

def home(request):
  return render(request, template_name='index.html')

def jeu(request, name):
  jeu = Jeux.objects.get(nom=name)
  tags = jeu.tags.all()
  return render(request, template_name='jeu.html', context={'jeu': jeu,'tags':tags})

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
            next = request.POST.get('next', '/lesJeux/listestudios/')
            return HttpResponseRedirect(next)
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
        form = StudioForm(instance=studio)
    return render(request, 'modifierstudio.html', {'form': form})

def supprimer_studio(request, nom):
    studio = get_object_or_404(Studio, nom=nom)
    studio.delete()
    return redirect('listestudios')

def tag(request, name):
  tag = Tag.objects.get(nom=name)
  return render(request, template_name='tag.html', context={'tag': tag})

def listetags(request):
  tags = Tag.objects.all()
  return render(request, template_name='listetags.html', context={'tags': tags})

def creer_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            next = request.POST.get('next', '/lesJeux/listetags/')
            return redirect(next)
    else:
        print("on est dans le else")
        form = TagForm()
    return render(request, 'creertag.html', {'form': form})

def modifier_tag(request, nom):
    tag = get_object_or_404(Tag, nom=nom)
    if request.method == 'POST':
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            return redirect('listetags')
    else:
        form = TagForm(instance=tag)
    return render(request, 'modifiertag.html', {'form': form})

def supprimer_tag(request, nom):
    tag = get_object_or_404(Tag, nom=nom)
    tag.delete()
    return redirect('listetags')

def search(request):
    if request.method == 'GET':
        query = request.GET.get('stringsearch')
        submitbutton = request.GET.get('submit')

        if query is not None:
            tags = Tag.objects.filter(nom__regex=r'{}'.format(query))
            jeux = Jeux.objects.filter(nom__regex=r'{}'.format(query))
            studios = Studio.objects.filter(nom__regex=r'{}'.format(query))

        else:
            tags = Tag.objects.all()
            jeux = Jeux.objects.all()
            studios = Studio.objects.all()

        return render(request, 'search.html',
                            {'tags': tags,
                             'jeux': jeux,
                             'studios': studios})