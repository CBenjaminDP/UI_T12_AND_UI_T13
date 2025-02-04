#crear formularios para cada modulo de la app
from .models import Producto
from django import forms

class ProductoForm(forms.ModelForm):
    class Meta:
        #definir el modelo
        model = Producto
        #definir los campos que se van a mostrar
        fields = ['nombre','precio','imagen']
        #definir los widgets
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Nombre del producto'
                }
            ),
            'precio': forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Precio del producto'
                }
            ),
            'imagen': forms.URLInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'URL de la imagen'
                }
            )
        }
        #definir las etiquetas
        labels = {
            'nombre':'Nombre del producto',
            'precio':'Precio del producto (MXN)',
            'imagen':'URL de la imagen'
        }
        #definir los mensajes de error
        error_messages = {
            'nombre':{
                'required':'El campo nombre es obligatorio'
            },
            'precio':{
                'required':'El campo precio es obligatorio'
            },
            'imagen':{
                'required':'El campo imagen es obligatorio'
            }
        }