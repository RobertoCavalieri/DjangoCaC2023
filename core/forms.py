# forms.py

from django import forms
from .models import Horario


class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = '__all__'  # Esto incluirá todos los campos del modelo en el formulario
