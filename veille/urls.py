from django.contrib.auth.views import LoginView
from django.urls import path
from .import views
from django.contrib.auth.views import LoginView

urlpatterns=[
    path("",views.Accueil,name="Acceuil"),
    path("inscription/",views.Inscription,name="Inscription"),
    path('connection/',view=LoginView.as_view(template_name="veille/main/home.html"),name="Login"),
    path('compte/',views.Compte,name="Compte"),
    path('contact/',views.Contact,name="Contact"),
    path('article/',views.afich_article,name="article")

]