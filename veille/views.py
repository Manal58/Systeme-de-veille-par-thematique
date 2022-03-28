from pyexpat.errors import messages

from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from pyexpat.errors import messages

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.shortcuts import render

from .fromulaire import CreateUserForm,UtiliForm
from .formulaire_requete import req
from .models import information,Requete,Veille,Article
from selenium1 import cree_fich
name_of_user=''
user_1 =''
def Contact(request):
    if request.method=="POST":
        form=UtiliForm(request.POST).save(commit=False)
        form1=Veille()
        form1.Prenom=user_1
        form1.Nom = form.Nom
        form1.Date_de_naissance = form.Date_de_naissance
        form1.Email = form1.Email
        form1.save()
        return redirect('Acceuil')
    else:
        form=UtiliForm()
    return render(request,'Contact.html',{'form':form})

def Inscription(request):
    if request.method == "POST":
        global user_1
        form = CreateUserForm(request.POST).save()
        user_1=form.username
        return redirect('Contact')
    else:
        form = CreateUserForm()
    return render(request, "main/inscription.html", {'form': form})


def Accueil(request):
    return render(request, "main/home.html", {})

def Contact(request):
    return render(request, "Contact.html", {})

def Compte(request):
    if request.method == "POST":
        form = req(request.POST).save(commit=False)
        veille=Veille.objects.get(Nom=name_of_user)
        form1= information()
        form1.Email = veille.Email
        form1.Nom_auteur = form.Nom_auteur
        form1.Domaine = form.Domaine
        form1.Mot_cle1 = form.Mot_cle1
        form1.Mot_cle2 = form.Mot_cle2
        form1.Mot_cle3 = form.Mot_cle3
        cree(form1.Email)
        form1.save()

        return redirect('/compte')
    else:
        form = req()
    return render(request, "main/compte.html", {'form': form})


def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        global name_of_user
        name_of_user=username
        if user is not None:
            veille=Veille.objects.get(Prenom=username)
            deja_vu(veille.Email)
            cree_fich(veille.Email)
            login(request, user)
            return redirect('Compte')
        else:
            messages.info(request, 'infos invalides')
    return render(request, "main/home.html")


def logoutUser(request):
    logout(request)
    return redirect('login')
def cree(email):
    info=information.objects.get(Email=email)
    req = ""
    author =info.Nom_auteur
    if (author != "None"):
        req = " AUTHOR :" + author

    field =info.Domaine
    if (field != "None"):
        req = field + req


    key = ""

    k = info.Mot_cle1
    if k != "None":
        key = k + " and " + key
    k = info.Mot_cle2
    if k != "None":
        key = k + " and " + key
    k = info.Mot_cle3
    if k != "None":
        key = k + " and " + key
    form=Requete()
    form.Email=info.Email
    form.requete=key+req
    form.save()

def afich_article(request) :
    veille=Veille.objects.get(Prenom=name_of_user)
    article=Article.objects.all()
    article_imp=[]
    for art in article :
        if(art.Email==veille.Email) :
            article_imp.append(art)
    article_imp.sort(key=lambda x:x.date_article,reverse=True)
    return render(request, 'article.html', {'form': article_imp})
def deja_vu(email) :
    veille=Veille.objects.get(Email=email)
    article = Article.objects.all()
    for art in article:
        if (art.Email == veille.Email):
            art.nouveau='deja_vu'



