from django.contrib import admin
from.models import Article
from .models import Veille
from.models import Requete
admin.site.register(Article)
admin.site.register(Requete)
admin.site.register(Veille)