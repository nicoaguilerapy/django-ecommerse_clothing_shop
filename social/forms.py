from django import forms
from .models import *

class FactForm(forms.ModelForm):
    class Meta:
        model = Fact
        fields = ['fact', 'value']

        widgets = {
            'value': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el Valor',
                    'id': 'value'
                }
            ),
            'fact': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'id': 'fact',
                    'readonly':''
                }
            ),
        }
        
class SocialForm(forms.ModelForm):
    class Meta:
        model = Social
        fields = ['social', 'url']

        widgets = {
            'url': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese la URL',
                    'id': 'url'
                }
            ),
            'social': forms.URLInput(
                attrs = {
                    'class':'form-control',
                    'id': 'social',
                    'readonly':'',
                }
            ),
        }
        
class NumberForm(forms.ModelForm):
    class Meta:
        model = Number
        fields = ['category', 'number', 'whatsapp', 'estado']

        widgets = {
            'category': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese la Categoria del Número',
                    'id': 'category'
                }
            ),
            'number': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el número formato (09xx)xxxxxx Sin espacios ni guiones',
                    'id': 'number'
                }
            ),

        }
        
class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['category', 'email', 'estado']

        widgets = {
            'category': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese la Categoria del Correo',
                    'id': 'category'
                }
            ),
            'email': forms.EmailInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el Correo',
                    'id': 'email'
                }
            ),

        }