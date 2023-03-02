from django.contrib import admin
from .models import Produit,Etudiant

# Register your models here.

class ProduitAdmin(admin.ModelAdmin):
    list_display = ('designation','quantite','prix')

admin.site.register(Produit,ProduitAdmin)
admin.site.register(Etudiant)