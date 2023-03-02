from django.db import models

# Create your models here.
class Produit(models.Model):
    designation = models.CharField(max_length=20)
    quantite = models.IntegerField()
    prix = models.FloatField()
    
    def __str__(self):
        return f"Produit N° "+str(self.id)+f"("+(self.designation)+f")"

class Etudiant(models.Model):
    nom= models.CharField(max_length=40)
    prenom= models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.nom