from django import forms
from django.forms import ModelForm
from .models import Profile

class ProfileForm(ModelForm):
    
    class Meta:
        model = Profile
        fields = ['avatar', 'nombre', 'apellido', 'celular']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs = {'class':'form-control mt-3', }),
            'nombre': forms.TextInput(attrs = {'class':'form-control bg-secondary text-white mt-3', }),
            'apellido': forms.TextInput(attrs = {'class':'form-control bg-secondary text-white mt-3', }),
            'celular': forms.TextInput(attrs = {'class':'form-control bg-secondary text-white mt-3', }),
        }
