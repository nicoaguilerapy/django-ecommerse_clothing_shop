from django import forms
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','description', 'content', 'image', 'status']

        widgets = {
            'title': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el Titulo',
                    'id': 'title'
                }
            ),
            'description': forms.Textarea(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese una descripción breve',
                    'rows':3,
                    'id': 'description'
                }
            ),
            'content': forms.Textarea(
                attrs = {
                    'class':'form-control',
                }
            ),
        }