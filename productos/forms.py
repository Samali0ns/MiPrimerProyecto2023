from django import forms

class ProductoForm(forms.Form):
    nombre=forms.CharField(max_length=100)
    precio=forms.FloatField()
    stock=forms.BooleanField(required=False)