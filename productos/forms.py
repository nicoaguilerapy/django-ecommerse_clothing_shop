from django import forms
from .models import Item, CoverPage, Category

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name','image','priority']

        widgets = {
            'name': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el Nombre',
                    'id': 'name'
                }
            ),
        }
        
class CoverPageForm(forms.ModelForm):
    class Meta:
        model = CoverPage
        fields = ['title','subtitle','button', 'priority', 'link', 'visibility', 'image']
        labels = {
        }
        widgets = {
            'title': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el Titulo',
                    'id': 'title'
                }
            ),
            'subtittle': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el subtitulo',
                    'id': 'subtittle'
                }
            ),
            'link': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el enlace',
                    'id': 'link'
                }
            ),
            'button': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el campo del Botón',
                    'id': 'button'
                }
            ),

        }

