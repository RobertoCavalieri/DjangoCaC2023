# models.py

from django.db import models
from django.contrib.auth.models import User


class Horario(models.Model):
    nombre = models.CharField(max_length=100)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    fecha = models.DateField()

    def __str__(self):
        return self.nombre

# Usando un modelo Proxy ya que no agrego nuevos campos
# class Persona(User):
#     class Meta:
#         proxy = True

class Persona(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre', )
    apellido = models.CharField(max_length=50, verbose_name='Apellido')
    mail = models.EmailField(max_length=150, verbose_name='Email')
    telefono = models.CharField(max_length=50, verbose_name='Teléfono', blank=True)
    usuario = models.OneToOneField(User,on_delete=models.CASCADE)

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    def __str__(self):
        return self.nombre_completo()


class Grupo(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre')
    miembros = models.ManyToManyField(Persona, related_name='grupos')

    def __str__(self):
        return f"{self.nombre}"


class Evento(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    descripcion = models.TextField(verbose_name='Descripcion')
    inicio = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name='Inicio')
    fin = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name='Fin')
    organizador = models.ForeignKey(Persona, on_delete=models.CASCADE)
    participantes = models.ManyToManyField(Grupo)

    def __str__(self):
        return f"{self.nombre} {self.inicio}"

