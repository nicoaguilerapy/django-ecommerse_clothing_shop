from django import forms
from .models import *

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['title','content', 'order', 'status']

        widgets = {
            'title': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el Nombre Corto',
                    'id': 'title'
                }
            ),
            'content': forms.Textarea(
                attrs = {
                    'class':'form-control',
                }
            ),
        }