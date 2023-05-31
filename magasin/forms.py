from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ProduitForm(ModelForm):
     class Meta : 
         model = Produit 
         fields = "__all__" 
  
     # #fields=['libelle','description'] 
class FournisseurForm(ModelForm):
    class Meta:
        model = Fournisseur
        fields = "__all__"




class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Prénom')
    last_name = forms.CharField(label='Nom')
    email = forms.EmailField(label='Adresse e-mail')
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name' , 'email')        
