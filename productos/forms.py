from django import forms
from .models import Producto, Portada, Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre','imagen_principal','orden']

        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el Nombre',
                    'id': 'nombre'
                }
            ),
        }
        
class PortadaForm(forms.ModelForm):
    class Meta:
        model = Portada
        fields = ['titulo','subtitulo','boton', 'orden', 'enlace', 'estado', 'imagen_principal']
        labels = {
            'precio_oferta': 'Precio Oferta',
            'categoria': 'Categorias',
        }
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
            'enlace': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el enlace',
                    'id': 'enlace'
                }
            ),
            'boton': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el campo del Botón',
                    'id': 'boton'
                }
            ),

        }
        
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['titulo','descripcion','precio','precio_oferta', 'oferta', 'categorias', 'orden', 'estado']
        labels = {
            'titulo': 'Titulo del Producto',
            'descripcion': 'Descripcion del Producto',
            'precio': 'Precio',
            'precio_oferta': 'Precio Oferta',
            'categorias': 'Categorias',
            'estado': 'Activo/Inactivo',
        }
        widgets = {
            'titulo': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el titulo',
                    'id': 'titulo'
                }
            ),
            'descripcion': forms.Textarea(
                attrs = {
                    'class':'form-control',
                    'rows':3,
                    'placeholder':'Ingrese la descripcion',
                    'id':'descripcion'
                }
            ),
            'categorias': forms.SelectMultiple(
                attrs = {
                    'class':'form-control'
                }
            ),
            'iamgen1': forms.ClearableFileInput(attrs = {'class':'form-control mt-3', }),
            'iamgen2': forms.ClearableFileInput(attrs = {'class':'form-control mt-3', }),
            'iamgen3': forms.ClearableFileInput(attrs = {'class':'form-control mt-3', }),
        }
