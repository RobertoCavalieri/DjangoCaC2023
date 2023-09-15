from django.db import models
from django.contrib.auth.models import User


class Horario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    dia_semana = models.CharField(max_length=10)  # Por ejemplo, Lunes, Martes, etc.
    hora_inicio = models.TimeField()
    hora_finalizacion = models.TimeField()
