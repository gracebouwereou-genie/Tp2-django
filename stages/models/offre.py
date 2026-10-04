from django.db import models

class Offre(models.Model):
    entreprise = models.ForeignKey("Entreprise", on_delete=models.PROTECT)

    titre = models.CharField(max_length=100)
    description = models.TextField()

    date_debut = models.DateField()
    date_fin = models.DateField()

    nb_places = models.IntegerField()

    competences = models.ManyToManyField("Competence")