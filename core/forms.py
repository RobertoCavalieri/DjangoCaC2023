# forms.py

from django import forms
from django.core.exceptions import ValidationError
from .models import Horario
from .models import Persona
from .models import Grupo


class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = '__all__'  # Esto incluirá todos los campos del modelo en el formulario


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



class EventoForm(forms.Form):
    nombre = forms.CharField(label='Nombre del Evento/tarea', required=True)
    fecha_inicio = forms.DateTimeField(input_formats=['%Y-%m-%dT%H:%M'], widget=forms.DateTimeInput(
        attrs={'type': 'datetime-local', 'class': 'form-control'}, format='%Y-%m-%dT%H:%M'))
    fecha_fin = forms.DateTimeField(input_formats=['%Y-%m-%dT%H:%M'], widget=forms.DateTimeInput(
        attrs={'type': 'datetime-local', 'class': 'form-control'}, format='%Y-%m-%dT%H:%M'))
    descripcion = forms.CharField(label='Descripción', widget=forms.Textarea())
    participantes = forms.ModelMultipleChoiceField(queryset=Grupo.objects.all())


# class PersonaForm(forms.ModelForm):
#     class Meta:
#         model = Persona
#         fields = '__all__'

class PersonaForm(forms.Form):
    nombre = forms.CharField(label='Nombre:', required=True)
    apellido = forms.CharField(label='Apellido:', required=True)
    mail = forms.EmailField(label='Email', required=True)
    telefono = forms.CharField(label='Teléfono',required=False)
    nombre_usuario = forms.CharField(label='Usuario', required=True)
    contraseña = forms.CharField(label='Contraseña', required=True, widget=forms.PasswordInput)
    contraseña_control = forms.CharField(label='Confirmación Contraseña', required=True, widget=forms.PasswordInput)


class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = '__all__'
