from django import forms
from .models import *

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['nombre','contenido', 'orden', 'estado']

        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el Nombre Corto',
                    'id': 'nombre'
                }
            ),
            'contenido': forms.Textarea(
                attrs = {
                    'class':'form-control',
                }
            ),
        }