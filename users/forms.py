from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña',
            'pattern': '^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9]{8,}$',
            'title': 'La contraseña debe contener al menos 8 caracteres, una mayúscula, una minúscula y un número',
            'required': True
        })
    )

    password2 = forms.CharField(
        label="Repetir Contraseña",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Repetir Contraseña',
            'pattern': '^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9]{8,}$',
            'title': 'La contraseña debe coincidir con la anterior',
            'required': True
        })
    )

    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'surname', 'control_number', 'age', 'tel', 'password1', 'password2']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email',
                'pattern': '^[a-zA-Z0-9]+@utez\.edu\.mx$',
                'title': 'Debes de ingresar un email de la UTEZ',
                'required': True
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre',
                'required': True
            }),
            'surname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apellido',
                'required': True
            }),
            'control_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número de control',
                'pattern':'^\d{5}[A-Za-z]{2}\d{3}$', 
                'title': 'Debes de ingresar un número de control válido por la utez',
                'required': True
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Edad',
                'min': 0,
                'required': True
            }),
            'tel': forms.TextInput(attrs={  
                'class': 'form-control',
                'placeholder': 'Teléfono',
                'pattern': '^\d{10}$',
                'required': True
            }),
        }
        

class CustomUserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Correo Electrónico", widget=forms.EmailInput)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        if email and password:
            user = authenticate(username=email, password=password)
        if not user:
            raise forms.ValidationError("Usuario o contraseña incorrectos.")
        return cleaned_data
