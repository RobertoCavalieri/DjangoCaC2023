# models.py

from django.db import models



class Horario(models.Model):
    nombre = models.CharField(max_length=100)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    fecha = models.DateField()

    def __str__(self):
        return self.nombre


class Persona(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField(max_length=100)
    telefono=models.CharField(max_length=20)
    mensaje=models.TextField()
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"