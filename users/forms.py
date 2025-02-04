from django import forms  
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.contrib.auth import authenticate
from .models import CustomUser  
import re

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'surname', 'control_number', 'age', 'tel', 'password1', 'password2']

        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'ejemplo@utez.edu.mx',
                'required': 'required'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre'
            }),
            'surname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apellido'
            }),
            'control_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número de Control',
                'required': 'required'
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Edad'
            }),
            'tel': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Teléfono'
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Contraseña',
                'required': 'required'
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Confirmar Contraseña',
                'required': 'required'
            }),
        }

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not re.match(r"^[a-zA-Z0-9._%+-]+@utez\.edu\.mx$", email):
            raise forms.ValidationError("Debes usar un correo de la UTEZ (ejemplo: 20223tn048@utez.edu.mx).")
        return email
        
    def clean_control_number(self):
        control_number = self.cleaned_data.get("control_number")
        if not re.match(r"^\d{5}[a-zA-Z]{2}\d{3}$", control_number):
            raise forms.ValidationError("El número de control debe seguir el formato UTEZ (ejemplo: 20223tn048).")
        return control_number

    # En la base de datos el control_number tiene como longitud 20 pero sabemos que una matricula de la UTEZ tiene 10 caracteres
    # De igual forma no se si esta es la forma correcta de utilizar los max y
    control_number = forms.CharField(
        max_length=10,  
        min_length=10,  
        validators=[
            MinLengthValidator(10, message="El número de control debe tener exactamente 10 caracteres."),
            MaxLengthValidator(10, message="El número de control debe tener exactamente 10 caracteres.")
        ],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Número de Control',
            'required': 'required'
        })
    )

    def clean_tel(self):
        tel = self.cleaned_data.get("tel")
        if not tel.isdigit() or len(tel) != 10:
            raise forms.ValidationError("El teléfono debe contener exactamente 10 dígitos numéricos.")
        return tel

    def clean_age(self):
        age = self.cleaned_data.get("age")
        if age < 0 or age > 120:
            raise forms.ValidationError("La edad debe estar entre 0 y 120 años.")
        return age

    def clean_password1(self):
        password = self.cleaned_data.get("password1")
        if len(password) < 8:
            raise forms.ValidationError("La contraseña debe tener al menos 8 caracteres.")
        if not any(char.isdigit() for char in password):
            raise forms.ValidationError("La contraseña debe contener al menos un número.")
        if not any(char.isupper() for char in password):
            raise forms.ValidationError("La contraseña debe contener al menos una letra mayúscula.")
        if not any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/~`" for char in password):
            raise forms.ValidationError("La contraseña debe contener al menos un carácter especial.")
        return password

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")

        return cleaned_data

class CustomUserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Correo electrónico",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'ejemplo@utez.edu.mx',
            'required': 'required'
        }),
        max_length=150
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña',
            'required': 'required'
        })
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if not re.match(r"^[a-zA-Z0-9._%+-]+@utez\.edu\.mx$", username):
            raise forms.ValidationError("Debes usar un correo de la UTEZ (ejemplo: 20223tn048@utez.edu.mx).")
        return username

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Usuario o contraseña incorrectos.")

        return cleaned_data