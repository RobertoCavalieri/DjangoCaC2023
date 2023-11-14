from django.contrib import admin
from core.models import Evento, Persona, Grupo, Horario

# Register your models here.
admin.site.register(Evento)
admin.site.register(Persona)
admin.site.register(Grupo)
admin.site.register(Horario)
