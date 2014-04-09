#-*- coding: utf-8 -*-
from django import forms
from models import Article

class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    envoyeur = forms.EmailField(label=u"Votre adresse mail")
    renvoi = forms.BooleanField(help_text=u"Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)
    
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        
class NouveauContactForm(forms.Form):
    nom = forms.CharField()
    adresse = forms.CharField(widget=forms.Textarea)
    photo = forms.ImageField()
    
class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    
class ProfilForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    email=forms.CharField(label="Adresse e-mail", max_length=75)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    
    