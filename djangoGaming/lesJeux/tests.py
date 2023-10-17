# A mettre dans le fichier tests.py de l'app Django

from datetime import date
from django.http import HttpRequest
from django.test import TestCase
from lesJeux.models import Jeux, Studio, Tag
from lesJeux.views import home, listejeux
from django.template.loader import render_to_string


class HomePageTestContent(TestCase):
    def test(self):
        '''Test Unitaire pour vérifier si le contenu de la page d'accueil est bien retourné par home()'''
        request = HttpRequest()
        response = home(request)
        expected_html = render_to_string('base.html')
        self.assertEqual(response.content.decode(), expected_html)

class listeJeuxTestContent(TestCase):
    def test(self):
        '''Test Unitaire pour vérifier si le contenu de la page liste jeux est bien retourné par listejeux()'''
        request = HttpRequest()
        response = listejeux(request)
        expected_html = render_to_string('listejeux.html')
        self.assertEqual(response.content.decode(), expected_html)


class ModeleJeuTest(TestCase):
    '''Test pour verifier la création de jeu dans le modèle'''
    def test(self, nom="test", description="le description", tags="test", date=date.today(), nomS="test", descriptionS="test", date_creation=date.today()):
        studio = Studio(nom=nomS, description=descriptionS, date_creation=date_creation)
        studio.save()
        
        jeu = Jeux(nom=nom, description=description, studio=studio, date=date)
        jeu.save()
        tag = jeu.tags.create(nom="test", description="desrciption test")
        tag.save()

        modele_db = Jeux.objects.get(nom=nom)

        self.assertEqual(jeu.nom, modele_db.nom)
        self.assertEqual(jeu.description, modele_db.description)
        self.assertEqual(jeu.studio, modele_db.studio)
        self.assertEqual(jeu.tags.all()[0], tag)
        self.assertEqual(jeu.date, modele_db.date)

class ModeleStudioTest(TestCase):
    '''Test pour verifier la création de Studio dans le modèle'''
    def test(self, nom="test", description="la description", date_creation=date.today()):
        studio = Studio(nom=nom, description=description, date_creation=date_creation)
        studio.save()

        modele_db = Studio.objects.get(nom=nom)

        self.assertEqual(studio.nom, modele_db.nom)
        self.assertEqual(studio.description, modele_db.description)
        self.assertEqual(studio.date_creation, modele_db.date_creation)

class ModeleTagTest(TestCase):
    '''Test pour verifier la création de Tag dans le modèle'''
    def test(self, nom="test", description="la description"):
        tag = Tag(nom=nom, description=description)
        tag.save()

        modele_db = Tag.objects.get(nom=nom)

        self.assertEqual(tag.nom, modele_db.nom)
        self.assertEqual(tag.description, modele_db.description)