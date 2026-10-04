from django.contrib import admin

# Register your models here.
from stages.models.entreprises import Entreprise



@admin.register(Entreprise)
class EntrepriseAdmin(admin.ModelAdmin):
    list_display = ["nom", "ville", "secteurs"]
    search_fields = ["nom", "ville"]

