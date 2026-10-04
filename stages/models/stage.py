from django.db import models

class Stage(models.Model):
    candidature = models.OneToOneField("Candidature", on_delete=models.PROTECT)

    tuteur = models.ForeignKey("TuteurEntreprise", on_delete=models.PROTECT)
    enseignant = models.ForeignKey("EnseignantReferent", on_delete=models.PROTECT)

    sujet = models.CharField(max_length=200)