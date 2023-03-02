from .models import Produit
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User


class ProduitForm(forms.ModelForm):
    designation = forms.CharField(label='Designation', widget=forms.TextInput(attrs={'class':'form-control'}))
    prix = forms.CharField(label='Prix', widget=forms.NumberInput(attrs={'class':'form-control'}))
    quantite = forms.CharField(label='Quantité', widget=forms.NumberInput(attrs={'class':'form-control'}))
    class Meta:
        model = Produit
        fields = ['designation','prix','quantite']
        
        
class InscriptionForm(UserCreationForm):
    username = forms.CharField(label='Utilisateur :',widget = forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label='Nom :',widget = forms.TextInput(attrs={'class':'form-control'}))
    first_name= forms.CharField(label='Prenoms :',widget = forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Mot de passe :',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirmer le mot de passe :',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(label='E-mail :',widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
         model = User
         fields = ['username','last_name','first_name','email','password1','password2','is_active']
        
class ConnForm(AuthenticationForm):
    username=UsernameField(label='Utilisateur :',widget =forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(label='Mot de passe :',widget =forms.PasswordInput(attrs={'class':'form-control'}))
