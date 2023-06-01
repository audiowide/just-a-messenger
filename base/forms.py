from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.forms import CharField, TextInput, PasswordInput
from .models import Profile

class CreateUserForm(ModelForm):
   username = CharField(widget=TextInput(attrs={'placeholder': 'Username'}))
   email = CharField(widget=TextInput(attrs={'placeholder': 'Email'}))
   password1 = CharField(widget=TextInput(attrs={'type': 'password', 'placeholder': ' Password'}))
   password2 = CharField(widget=TextInput(attrs={'type': 'password', 'placeholder': 'Repeat your password'}))
   
   class Meta:
      model = User
      fields = ['username', 'email', 'password1', 'password2']