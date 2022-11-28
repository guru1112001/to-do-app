from django import forms
from .models import account
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class login_form(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput)


class register_form(UserCreationForm):
    email=forms.EmailField()
    
    class meta:
        Model=User
        fields=["username","email", "password1","password2"]




