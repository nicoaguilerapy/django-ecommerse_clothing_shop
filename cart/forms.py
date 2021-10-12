from django import forms
from .models import *

class CouponForm(forms.ModelForm):
    class Meta:
        model = Coupon
        fields = ['code','amount', 'percentage', ]

        widgets = {
            'code': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el Nombre Corto',
                    'id': 'code'
                }
            ),
            'amount': forms.NumberInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el Monto Fijo',
                    'id': 'amount'
                }
            ),
            'percentage': forms.NumberInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el Porcentaje',
                    'id': 'percentage'
                }
            ),
        }
        
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['id']