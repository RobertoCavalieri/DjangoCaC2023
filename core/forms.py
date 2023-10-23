# forms.py

from django import forms
from django.core.exceptions import ValidationError
from datetime import datetime
from .models import Horario

# Opciones de los desplegables.
OPCIONES_COLOR = [('fc-bg-default', 'default'), ('fc-bg-blue', 'azul'), (
    'fc-bg-lightgreen', 'verde'), ('fc-bg-pinkred', 'Rosado'), ('c-bg-deepskyblue', 'Azul Cielo'), ]
OPCIONES_ICONO = [('circle', 'circulo'), ('cog', 'cog'), ('group',
                                                          'grupo'), ('suitcase', 'portafolio'), ('calendar', 'calendario'),]


class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = '__all__'  # Esto incluirá todos los campos del modelo en el formulario


class AltaEventoForm(forms.Form):
    ename = forms.CharField(label='Nombre de la tarea', widget=forms.TextInput(
        attrs={'class': 'form-control'}), required=True)
    # edate = forms.CharField(label='Fecha de la tarea', widget=forms.TextInput(attrs={'class': 'datetimepicker form-control'}), required=True)
    edate = forms.DateTimeField(label='Fecha de la tarea', widget=forms.DateTimeInput(
        attrs={'class': 'datetimepicker form-control'}), required=True)
    edesc = forms.CharField(label='Descripción de la tarea', widget=forms.Textarea(
        attrs={'class': 'form-control'}))
    ecolor = forms.ChoiceField(label='Color', choices=OPCIONES_COLOR, widget=forms.Select(
        attrs={'class': 'form-control'}))
    eicon = forms.ChoiceField(label='Icono', choices=OPCIONES_ICONO, widget=forms.Select(
        attrs={'class': 'form-control'}))

    def clean_edate(self):
        # validamos que la fecha tenga un formáto válido.
        if self.cleaned_data['edate'] < datetime.now():
            raise ValidationError("La fecha no puede ser enterior a hoy.")

        return self.cleaned_data['edate']

    def clean(self):
        # # Este if simula una busqueda en la base de datos
        # if self.cleaned_data['edate'] == '2023-12-15':
        #     raise ValidationError("Ya tiene una cita en este horario")

        return self.cleaned_data


class EventoForm(forms.Form):
    nombre = forms.CharField(label='Nombre del Evento/tarea', required=True)
    fecha_inicio = forms.DateTimeField(input_formats=['%Y-%m-%dT%H:%M'], widget=forms.DateTimeInput(
        attrs={'type': 'datetime-local', 'class': 'form-control'}, format='%Y-%m-%dT%H:%M'))
    fecha_fin = forms.DateTimeField(input_formats=['%Y-%m-%dT%H:%M'], widget=forms.DateTimeInput(
        attrs={'type': 'datetime-local', 'class': 'form-control'}, format='%Y-%m-%dT%H:%M'))
    descripcion = forms.CharField(label='Descripción', widget=forms.Textarea())
    # color = forms.ChoiceField(
    #     label='Color', choices=OPCIONES_COLOR, widget=forms.Select())
    # icono = forms.ChoiceField(
    #     label='Icono', choices=OPCIONES_ICONO, widget=forms.Select())
