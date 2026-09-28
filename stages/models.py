from django.db import models

# Create your models here.
class Entreprise(models.Model):
    SECTEURS = [
        ('banque', 'Banque'),
        ('telecom', 'Télécom'),
        ('informatique', 'Informatique'),
    ]

    nom = models.CharField(max_length=120, unique=True)
    ville = models.CharField(max_length=80)
    secteur = models.CharField(max_length=80, choices=SECTEURS)
    email = models.EmailField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['nom', 'ville'],
                name='unique_entreprise_nom_ville'
            )
        ]

    def __str__(self):
        return f"{self.nom} ({self.ville})"