from django.db import models
from .personnes import Personne

class TuteurEntreprise(Personne):
    entreprise = models.ForeignKey("Entreprise", on_delete=models.PROTECT)