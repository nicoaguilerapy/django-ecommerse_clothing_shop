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

class DestacadoForm(forms.ModelForm):
    class Meta:
        model = Destacado
        fields = ['titulo','subtitulo', 'orden', 'estado', 'pagina']

        widgets = {
            'titulo': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el Titulo',
                    'id': 'titulo'
                }
            ),
            'subtitulo': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el subtitulo',
                    'id': 'subtitulo'
                }
            ),

        }