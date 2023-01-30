from django import forms
from .models import Producto,Categorias

class ProductoForm(forms.Form):
    nombre=forms.CharField(max_length=100)
    precio=forms.FloatField()
    stock=forms.BooleanField(required=False)


class AgregaProducto(forms.ModelForm):
    class Meta:
        model=Producto
        fields = '__all__'
