from django import forms
from .models import todo

class create_todo(forms.ModelForm):

     class Meta:
        model= todo
        fields='__all__'
