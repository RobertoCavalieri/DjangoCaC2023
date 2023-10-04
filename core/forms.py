# forms.py

from django import forms
from .models import Horario
from django.core.exceptions import ValidationError


class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = '__all__'  # Esto incluirá todos los campos del modelo en el formulario

class ContactoForm(forms.Form):
    nombre=forms.CharField(label="Nombre", widget=forms.TextInput(attrs={'class':'estilo_input'}), required=True)
    apellido=forms.CharField(label="Apellido", widget=forms.TextInput(attrs={'class':'estilo_input'}), required=True)
    mail=forms.EmailField(label="Email", widget=forms.TextInput(attrs={'class':'estilo_input'}), required=True)
    telefono = forms.IntegerField(label="Teléfono",  widget=forms.TextInput(attrs={'class':'estilo_input'}), required=True)
    Mensaje=forms.CharField(widget=forms.Textarea(attrs={'class':'estilo_input'}) )
    
    
class ContactoForm(forms.Form):
    nombre=forms.CharField(label="Nombre", widget=forms.TextInput(attrs={'class':'estilo_input'}), required=True)
    apellido=forms.CharField(label="Apellido", widget=forms.TextInput(attrs={'class':'estilo_input'}), required=True)
    mail=forms.EmailField(label="Email", widget=forms.TextInput(attrs={'class':'estilo_input'}), required=True)
    telefono = forms.CharField(label="Teléfono", widget=forms.TextInput(attrs={'class':'estilo_input'}), required=True)
    Mensaje=forms.CharField(widget=forms.Textarea(attrs={'class':'estilo_input'}), required=True)

    

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if len(nombre) < 2:
            raise ValidationError('El nombre debe tener al menos 2 caracteres.')
        return nombre

    def clean_apellido(self):
        apellido = self.cleaned_data['apellido']
        if len(apellido) < 2:
            raise ValidationError('El apellido debe tener al menos 2 caracteres.')
        return apellido    
    
    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        if not telefono.isdigit():
            raise ValidationError('El número de teléfono debe contener solo dígitos.')
        elif  len(telefono)>15:
            raise ValidationError('El número de teléfono debe contener hasta 15 dígitos.')
        return telefono
    
    
    def clean(self):
        if self.cleaned_data['nombre'] =='carlos' and self.cleaned_data['apellido'] =='lopez':
            raise ValidationError("El usuario Carlos Lopez ya existe")
        return self.cleaned_data