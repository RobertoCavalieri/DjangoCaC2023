# models.py

from django.db import models


class Horario(models.Model):
    nombre = models.CharField(max_length=100)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    fecha = models.DateField()

    def __str__(self):
        return self.nombre
