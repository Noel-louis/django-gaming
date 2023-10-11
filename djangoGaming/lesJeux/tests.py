# A mettre dans le fichier tests.py de l'app Django

from datetime import date
from django.http import HttpRequest
from django.test import TestCase
from lesJeux.models import Jeux
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
    '''Test pour verifier la création dans le modèle'''
    def test(self, nom="test", description="le description", studio="un studio", tags="test", date=date.today()):
        jeu = Jeux(nom=nom, description=description, studio=studio, tags=tags, date=date)
        jeu.save()

        modele_db = Jeux.objects.get(nom=nom)

        self.assertEqual(jeu.nom, modele_db.nom)
        self.assertEqual(jeu.description, modele_db.description)
        self.assertEqual(jeu.studio, modele_db.studio)
        self.assertEqual(jeu.tags, modele_db.tags)
        self.assertEqual(jeu.date, modele_db.date)
