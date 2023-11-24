from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import ListView, CreateView


from datetime import datetime

# from core.forms import AltaEventoForm
from core.forms import EventoForm
from core.forms import ContactoForm
from core.forms import PersonaForm
from core.models import Evento
from core.models import Persona
from core.models import Grupo
from django.contrib.auth.models import User, UserManager


# Create your views here.
def index(request):
    context = {
        'nombre_usuario': 'Jose Lopez',
        'fecha': datetime.now(),
        'es_instructor': True,
    }
    return render(request, 'core/index.html', context)


def contacto(request):
    if request.method=="POST":
        formulario= ContactoForm(request.POST)

        if formulario.is_valid():
            messages.info(request,'Formulario enviado con exito')
            return redirect(reverse('contacto'))
    else: #GET
        formulario= ContactoForm()

    context={
        'contacto_form': formulario
    }
    return render(request, "core/contacto.html", context)

@login_required
def alta_evento(request):
    if request.method == 'POST':
        # Instanciamos un formulario con datos
        formulario = EventoForm(request.POST)
        # Validarlo
        if formulario.is_valid():
            # Dar de alta la info
            nuevo_evento = Evento(
                nombre = formulario.cleaned_data['nombre'],
            #El organizador es la persona que esta dando de alta el evento
            #por ahora lo dejamos con cualquier persona.
                organizador = request.user.persona,
                descripcion = formulario.cleaned_data['descripcion'],
                inicio = formulario.cleaned_data['fecha_inicio'],
                fin = formulario.cleaned_data['fecha_fin']
            )
            nuevo_evento.save()
            nuevo_evento.participantes.set(formulario.cleaned_data['participantes'])
            messages.info(request, "Evento cargado con éxito")
            return redirect(reverse('calendario_individual'))
    else:   #GET
        formulario = EventoForm()

    context = {
        'evento_form': formulario
    }
    return render(request, 'core/eventos_alta.html', context)


class EventoListView(LoginRequiredMixin, ListView):
    model = Evento
    context_object_name = 'event_list'
    template_name = 'core/calendario_individual.html'

    def get_queryset(self):
        evento_organizador = Evento.objects.filter(organizador = self.request.user.persona)
        evento_participante = Evento.objects.filter(participantes__miembros = self.request.user.persona)
        return  evento_participante.union(evento_organizador)


# class PersonaCreateView(PermissionRequiredMixin, CreateView):
#     permission_required = 'core.add_persona'
#     model = Persona
#     template_name = 'core/alta_persona.html'
#     success_url = 'listado'
#     fields = '__all__'


class PersonaListView(LoginRequiredMixin, ListView):
    model = Persona
    context_object_name = 'listado_personas'
    template_name = 'core/personas_listado.html'


class GrupoCreateView(LoginRequiredMixin, CreateView):
    model = Grupo
    template_name = 'core/alta_grupo.html'
    success_url = 'listado'
    fields = '__all__'


class GrupoListView(LoginRequiredMixin, ListView):
    model = Grupo
    context_object_name = 'listado_grupos'
    template_name = 'core/grupos_listado.html'


@login_required
def grupo_detalle(request,id_grupo):
    print(id_grupo)
    grupo = Grupo.objects.filter(id = int(id_grupo))
    print(grupo)
    miembros = grupo[0].miembros.all()

    context = {
        'nombre_grupo' : grupo[0].nombre,
        'lista_integrantes' : miembros
    }

    return render(request, 'core/grupo_detalle.html', context)


def alta_persona(request):
    if request.user.is_authenticated and not request.user.has_perm('core.add_persona'):
        return render(request, "core/login_error.html")

    if request.method == 'POST':
        # Instanciamos un formulario con datos
        formulario = PersonaForm(request.POST)
        # Validarlo
        if formulario.is_valid():
            nueva_persona = Persona(
                nombre = formulario.cleaned_data['nombre'],
                apellido = formulario.cleaned_data['apellido'],
                mail = formulario.cleaned_data['mail'],
                telefono = formulario.cleaned_data['telefono'],
            )
            nuevo_usuario = User.objects.create_user(
                username=formulario.cleaned_data['nombre_usuario'],
                password=formulario.cleaned_data['contraseña']
            )
            nueva_persona.usuario = nuevo_usuario
            nueva_persona.save()
            if request.user.is_authenticated:
                messages.info(request, "Persona cargada con éxito")
                return redirect(reverse('personas_listado'))
            else:
                messages.info(request, "Registro exitoso, ingrese al sistema con su usuario")
                return redirect(reverse('login'))
    else:   #GET
        formulario = PersonaForm()

    context = {
        'persona_form': formulario
    }
    return render(request, 'core/alta_persona.html', context)