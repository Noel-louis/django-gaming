from django.db import models

class Jeux(models.Model):
    nom = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    studio = models.CharField(max_length=250)
    tags = models.CharField(max_length=250)
    date = models.DateField()

    def __str__(self):
        return self.nom
    
class Studio(models.Model):
    nom = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    date_creation = models.DateField()
    jeux_cree = models.ForeignKey(Jeux, on_delete=models.CASCADE, null=True, related_name="jeux_cree")

    def __str__(self):
        return self.nom