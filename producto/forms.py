from django import forms
from .models import Producto

class ProductoFomr(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"
    