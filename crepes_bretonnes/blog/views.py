#-*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import redirect
from datetime import datetime
from django.shortcuts import render, get_object_or_404
from blog.models import Article
from blog.models import Contact
from blog.forms import ContactForm
from blog.forms import ArticleForm
from blog.forms import ConnexionForm
from blog.forms import ProfilForm
from blog.forms import NouveauContactForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout                                                                  
from django.shortcuts import render                                                                     
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def home(request):
  text = """<h1>Bienvenue sur mon blog !</h1>
            <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>"""
  return HttpResponse(text)
  
def view_article(request, id_article):
    """ Vue qui affiche un article selon son identifiant (ou ID, ici un numéro). Son ID est le second paramètre de la fonction 
        (pour rappel, le premier paramètre est TOUJOURS la requête de l'utilisateur) """
   
    if int(id_article) > 100:
        raise Http404
    elif int(id_article) < 10:
        return redirect(view_redirection)
    else:
        text = "Vous avez demandé l'article n°{0} !".format(id_article)
        return HttpResponse(text)
        
def dire_bonjour(request):                                                                              
    if request.user.is_authenticated():                                                                 
        return HttpResponse("Salut, {0} !".format(request.user.username))                               
    return HttpResponse("Salut, anonyme.")


def list_articles(request, month, year):
    """ Liste des articles d'un mois précis. """

    text = "Vous avez demandé les articles de {0} {1}.".format(month, year)
    return HttpResponse(text)
    
def view_redirection(request):
    return HttpResponse(u"Vous avez été redirigé.")
    
def tpl(request):
    return render(request, 'blog/tpl.html', {'current_date': datetime.now()})
    
def addition(request, nombre1, nombre2):
    total = int(nombre1) + int(nombre2)
    # retourne nombre1, nombre2 et la somme des deux
    return render(request, 'blog/addition.html', locals())
    
    
def image(request):
    return render(request, 'blog/image.html')
    
def lire(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'blog/lire.html', {'article':article})
    
def contact(request):
    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = ContactForm(request.POST)  # Nous reprenons les données

        if form.is_valid(): # Nous vérifions que les données envoyées sont valides

            # Ici nous pouvons traiter les données du formulaire
            sujet = form.cleaned_data['sujet']
            message = form.cleaned_data['message']
            envoyeur = form.cleaned_data['envoyeur']
            renvoi = form.cleaned_data['renvoi']

            # Nous pourrions ici envoyer l'e-mail grâce aux données que nous venons de récupérer

            envoi = True

    else: # Si ce n'est pas du POST, c'est probablement une requête GET
        form = ContactForm()  # Nous créons un formulaire vide

    return render(request, 'blog/message.html', locals())
    
def message(request,sujet,message):
    return render(request, 'blog/message.html',locals())
    
def formulaire(request):
    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = ArticleForm(request.POST)  # Nous reprenons les données

        if form.is_valid(): # Nous vérifions que les données envoyées sont valides

            # Ici nous pouvons traiter les données du formulaire
            titreM = form.cleaned_data['titre']
            auteurM = form.cleaned_data['auteur']
            contenuM = form.cleaned_data['contenu']
            categorieM=form.cleaned_data['categorie']
            article = Article(titre=titreM, auteur=auteurM,contenu=contenuM,categorie=categorieM).save()
            # Nous pourrions ici envoyer l'e-mail grâce aux données que nous venons de récupérer

            envoi = True

    else: # Si ce n'est pas du POST, c'est probablement une requête GET
        form = ArticleForm()  # Nous créons un formulaire vide

    return render(request, 'blog/formulaire.html', locals())
    
def nouveau_contact(request):
    sauvegarde = False

    if request.method == "POST":
           form = NouveauContactForm(request.POST, request.FILES)
           if form.is_valid():
                   contact = Contact()
                   contact.nom = form.cleaned_data["nom"]
                   contact.adresse = form.cleaned_data["adresse"]
                   contact.photo = form.cleaned_data["photo"]
                   contact.save()

                   sauvegarde = True
    else:
           form = NouveauContactForm()

    return render(request, 'blog/nouveau_contact.html',locals())
    
def voir_contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'blog/voir_contacts.html',{'contacts':contacts})
    
def creation(request):
    sauvegarde = False
    error=False

    if request.method == "POST":
        form = ProfilForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(nom, email,password)
            try:
                user.save()
                sauvegarde = True
                userT = authenticate(username=nom, password=password)
                if userT:  # Si l'objet renvoyé n'est pas None
                    login(request, userT)  # nous connectons l'utilisateur
                else: #sinon une erreur sera affichée
                    error = True
            except:
                error=True
                    
                    
                    
    else:
        form = ProfilForm()

    return render(request, 'blog/creation.html',locals())
    
def connexion(request):
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]  # Nous récupérons le nom d'utilisateur
            password = form.cleaned_data["password"]  # … et le mot de passe
            user = authenticate(username=username, password=password)  #Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
            else: #sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'blog/connexion.html',locals())
    
def deconnexion(request):                                                                               
    logout(request)                                                                                     
    return redirect(reverse(connexion))
    
@login_required(login_url='/blog/connexion/')
def confirmation(request):
    return render(request, 'blog/confirmation.html')
