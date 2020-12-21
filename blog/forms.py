from django import forms
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo','descripcion', 'contenido', 'imagen', 'estado']

        widgets = {
            'titulo': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el Titulo',
                    'id': 'titulo'
                }
            ),
            'descripcion': forms.Textarea(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese una descripción breve',
                    'rows':3,
                    'id': 'descripcion'
                }
            ),
            'contenido': forms.Textarea(
                attrs = {
                    'class':'form-control',
                }
            ),
        }