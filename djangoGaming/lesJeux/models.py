from django.db import models

class Jeux(models.Model):
    nom = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    studio = models.ForeignKey('Studio', on_delete=models.CASCADE, null=True, related_name="studio")
    tags = models.ManyToManyField('Tag', related_name="tags")
    date = models.DateField()

    def __str__(self):
        return self.nom

class Studio(models.Model):
    nom = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    date_creation = models.DateField()

    def __str__(self):
        return self.nom
    
class Tag(models.Model):
    nom = models.CharField(max_length=250)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.nom