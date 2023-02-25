from django import forms
from .models import todo

class create_todo(forms.ModelForm):
   title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))
   class Meta:
        model= todo
        fields='__all__'
