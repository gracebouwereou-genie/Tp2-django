from django.contrib import admin

# Register your models here.
from stages.models.entreprises import Entreprise
from stages.models.etudiant import Etudiant
from stages.models.enseignant_referent import EnseignantReferent
from stages.models.competence import Competence
from stages.models.offre import Offre
from stages.models.tuteur_entreprise import TuteurEntreprise
from stages.models.candidature import Candidature


@admin.register(Entreprise)
class EntrepriseAdmin(admin.ModelAdmin):
    list_display = ["nom", "ville", "secteurs"]
    search_fields = ["nom", "ville"]

@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    search_fields = ["nom", "promotion"]

@admin.register(EnseignantReferent)
class EnseignantReferentAdmin(admin.ModelAdmin):
    search_fields = ["nom"]

@admin.register(Competence)
class CompetenceAdmin(admin.ModelAdmin):
    search_fields = ["libelle"]

@admin.register(Offre)
class OffreAdmin(admin.ModelAdmin):
    search_fields = ["titre", "competences"]

@admin.register(TuteurEntreprise)
class OffreAdmin(admin.ModelAdmin):
    search_fields = ["entreprise"]

@admin.register(Candidature)
class OffreAdmin(admin.ModelAdmin):
    search_fields = ["etudiant", "offre"]