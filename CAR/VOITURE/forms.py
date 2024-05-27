from django import forms
from .models import user
from django.contrib.auth.forms import UserCreationForm

class ProductForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ['id', 'email', 'nom','prenom','mot_de_passe']

