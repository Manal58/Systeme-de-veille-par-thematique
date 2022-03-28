from django.apps import AppConfig



class RequetesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'requetes'


class ArticleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'article'

class VeilleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'veille'