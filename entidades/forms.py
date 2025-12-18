from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import *

class CursoForm(forms.Form):
    nombre = forms.CharField(max_length=100, label="Nombre del Curso")
    comision = forms.IntegerField(label="Número de Comisión", required=True)
    profesor = forms.ModelChoiceField(queryset=Profesor.objects.all(), label="Profesor", required=False)

class ProfesorForm(forms.Form):
    nombre = forms.CharField(max_length=60, label="Nombre")
    apellido = forms.CharField(max_length=60, label="Apellido")
    email = forms.EmailField(label="Email")
    profesion = forms.CharField(max_length=50, label="Profesión")

class RegistroForm(UserCreationForm):
    email = forms.EmailField(label="Correo Electrónico", required=True)
    first_name = forms.CharField(label="Nombre", max_length=30, required=True)
    last_name = forms.CharField(label="Apellido", max_length=30, required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "first_name", "last_name")

class ProfileForm(UserChangeForm):
    email = forms.EmailField(label="Correo Electrónico", required=True)
    first_name = forms.CharField(label="Nombre", max_length=30, required=True)
    last_name = forms.CharField(label="Apellido", max_length=30, required=True)

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name")

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'avatar']      

