from django.db import models

class Candidature(models.Model):

    STATUT_CHOICES = [
        ('deposee', 'Déposée'),
        ('retenue', 'Retenue'),
        ('refusee', 'Refusée'),
    ]

    etudiant = models.ForeignKey("Etudiant", on_delete=models.CASCADE)
    offre = models.ForeignKey("Offre", on_delete=models.CASCADE)

    date_depot = models.DateField(auto_now_add=True)
    statut = models.CharField(max_length=10, choices=STATUT_CHOICES)

    class Meta:
        unique_together = ('etudiant', 'offre')