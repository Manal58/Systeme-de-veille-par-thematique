from django.contrib.admin import models
from django.contrib.auth.models import User
from django.forms import ModelForm, forms

from django.contrib.auth.forms import UserCreationForm
from.models import Veille

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','password1', 'password2']

class UtiliForm(ModelForm):
	class Meta:
		model=Veille
		fields=['Nom','Date_de_naissance','Email','Confirmation_email']