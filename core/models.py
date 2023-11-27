from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from django.utils import timezone

class Horario(models.Model):
    nombre = models.CharField(max_length=100)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    fecha = models.DateField()

    def __str__(self):
        return self.nombre


class Persona(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    apellido = models.CharField(max_length=50, verbose_name='Apellido')
    mail = models.EmailField(max_length=150, verbose_name='Email')
    telefono = models.CharField(max_length=50, verbose_name='Teléfono', blank=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    def encontrar_tiempos_libres(self, fecha_inicio, fecha_fin):
        fecha_inicio = timezone.make_aware(fecha_inicio)
        fecha_fin = timezone.make_aware(fecha_fin)

        eventos = self.evento_set.filter(
            Q(inicio__range=(fecha_inicio, fecha_fin)) | Q(fin__range=(fecha_inicio, fecha_fin))
        )

        intervalos_ocupados = [(evento.inicio, evento.fin) for evento in eventos]

        intervalo_libre = [(fecha_inicio, fecha_fin)]

        for ocupado_inicio, ocupado_fin in intervalos_ocupados:
            nuevo_intervalo_libre = []
            for libre_inicio, libre_fin in intervalo_libre:
                if libre_inicio < ocupado_inicio:
                    nuevo_intervalo_libre.append((libre_inicio, min(ocupado_inicio, libre_fin)))
                if libre_fin > ocupado_fin:
                    nuevo_intervalo_libre.append((max(ocupado_fin, libre_inicio), libre_fin))
            intervalo_libre = nuevo_intervalo_libre

        return intervalo_libre

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
