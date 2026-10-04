from django.db import models
from .personne import Personne

class Etudiant(Personne):
    matricule = models.CharField(max_length=50)
    promotion = models.IntegerField()
    competences = models.ManyToManyField("Competence")