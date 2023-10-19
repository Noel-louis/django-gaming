# A mettre dans le fichier tests.py de l'app Django

from datetime import date
from django.http import HttpRequest
from django.test import TestCase
from lesJeux.views import home, listejeux, tag
from lesJeux.models import Jeux, Studio, Tag
from django.template.loader import render_to_string
from django.urls import reverse


class ModeleJeuTest(TestCase):
    '''Test pour verifier la création de jeu dans le modèle'''
    def test(self, nom="test", description="le description", date=date.today(), nomS="test", descriptionS="test", date_creation=date.today()):
        
        # on créé un studio et on l'ajoute dans la BD
        studio = Studio(nom=nomS, description=descriptionS, date_creation=date_creation)
        studio.save()
        
        # on créé le jeu et on l'ajoute dans la BD
        jeu = Jeux(nom=nom, description=description, studio=studio, date=date)
        jeu.save()
        tag = jeu.tags.create(nom="test", description="desrciption test")
        tag.save()

        modele_db = Jeux.objects.get(nom=nom)

        # test si il y a jeu dans la table
        self.assertEqual(Jeux.objects.count(), 1)

        # test sur les arguments du jeu
        self.assertEqual(jeu.nom, modele_db.nom)
        self.assertEqual(jeu.description, modele_db.description)
        self.assertEqual(jeu.studio, modele_db.studio)
        self.assertEqual(jeu.tags.all()[0], tag)
        self.assertEqual(jeu.date, modele_db.date)

        # on supprime le jeu
        jeu.delete()

        # test si le jeu est bien suprimer
        self.assertEqual(Jeux.objects.count(), 0)



class ModeleStudioTest(TestCase):
    '''Test pour verifier la création de Studio dans le modèle'''
    def test(self, nom="test", description="la description", date_creation=date.today()):

        # on créé un studio et on l'ajoute dans la BD
        studio = Studio(nom=nom, description=description, date_creation=date_creation)
        studio.save()

        # test si il y a studio dans la table
        self.assertEqual(Studio.objects.count(), 1)

        modele_db = Studio.objects.get(nom=nom)

        # test sur les arguments du studio
        self.assertEqual(studio.nom, modele_db.nom)
        self.assertEqual(studio.description, modele_db.description)
        self.assertEqual(studio.date_creation, modele_db.date_creation)

        # on supprime le studio
        studio.delete()

        # test si le studio est bien suprimer
        self.assertEqual(Studio.objects.count(), 0)



class ModeleTagTest(TestCase):
    '''Test pour verifier la création de Tag dans le modèle'''
    def test(self, nom="test", description="la description"):

        # on créé un tag et on l'ajoute dans la BD
        tag = Tag(nom=nom, description=description)
        tag.save()

        modele_db = Tag.objects.get(nom=nom)

        # test sur les arguments du tag
        self.assertEqual(tag.nom, modele_db.nom)
        self.assertEqual(tag.description, modele_db.description)

        # on supprime le tag
        tag.delete()

        # test si le tag est bien suprimer
        self.assertEqual(Tag.objects.count(), 0)


class UrlTest(TestCase):
    '''Test pour verifier les urls'''
   
    def testUrlListeJeu(self):
        '''Test Unitaire pour vérifier si le contenu de la page liste jeux est bien retourné par listejeux()'''
        request = HttpRequest()
        response = listejeux(request)
        expected_html = render_to_string('listejeux.html')
        self.assertEqual(response.content.decode(), expected_html)

    def testUrlHome(self):
        '''Test Unitaire pour vérifier si le contenu de la page d'accueil est bien retourné par home()'''
        request = HttpRequest()
        response = home(request)
        expected_html = render_to_string('index.html')
        self.assertEqual(response.content.decode(), expected_html)