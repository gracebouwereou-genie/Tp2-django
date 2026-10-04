from django.db import models
from .personne import Personne

class TuteurEntreprise(Personne):
    entreprise = models.ForeignKey("Entreprise", on_delete=models.PROTECT)