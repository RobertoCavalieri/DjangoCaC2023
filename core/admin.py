from django.contrib import admin
from core.models import Evento, Persona, Grupo, Horario

# Register your models here.


class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'mail')
    list_editable = ('nombre', 'apellido')
    list_display_links = ['mail']
    search_fields = ['apellido']


class GrupoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field == 'integrantes':
            kwargs["queryset"] = Persona.objects.filter().order_by("apellido")

        return super().formfield_for_manytomany(db_field, request, **kwargs)


class EventoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'inicio', 'fin', 'organizador')
    # list_editable = ('nombre', 'inicio', 'fin')

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field == 'participantes':
            kwargs["queryset"] = Grupo.objects.filter().order_by("nombre")

        return super().formfield_for_manytomany(db_field, request, **kwargs)


admin.site.register(Evento, EventoAdmin)
admin.site.register(Persona, PersonaAdmin)
admin.site.register(Grupo, GrupoAdmin)
admin.site.register(Horario)


