from django.views.generic import ListView, CreateView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse

from core.forms import HorarioForm
from django.urls import reverse
from datetime import datetime

from core.forms import AltaEventoForm
from core.forms import EventoForm
from core.models import Evento
from core.models import Persona

from .forms import ContactoForm


def index(request):
    context = {
        'nombre_usuario': 'Jose Lopez',
        'fecha': datetime.now(),
        'es_instructor': True,
    }
    return render(request, 'core/index.html', context)

def evento(request):
    if request.method == 'POST':
        # Instanciamos un formulario con datos
        formulario = EventoForm(request.POST)

                # Validarlo
        if formulario.is_valid():
            # Dar de alta la info
            nuevo_evento = Evento(
                nombre = formulario.cleaned_data['nombre'],
                descripcion = formulario.cleaned_data['descripcion'],
                inicio = formulario.cleaned_data['fecha_inicio'],
                fin = formulario.cleaned_data['fecha_fin']
                # participantes=formulario.cleaned_data['participantes'] #Así no funca.
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
    return render(request, 'core/evento.html', context)


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


def gestion_grupos(request):
    listado = [
        'Jose Lopez',
        'Maria Del Cerro',
        'Jose Lopez',
    ]

    context = {
        'nombre_usuario': 'Jose Lopez',
        'fecha': datetime.now(),
        'es_instructor': True,
        'listado_alumnos': listado,
        'cant_inscriptos': len(listado),
    }

    return render(request, 'core/calendario_grupo.html', context)


def grupo_detalle(request, nombre_alumno):
    context = {
        'nombre_alumno': nombre_alumno,
    }
    return render(request, 'core/grupo_detalle.html')


def calendario_grupo(request, calendario_data=None):
    context = {
        'nombre_usuario': 'Jose Lopez',
        'fecha': datetime.now(),
        'es_instructor': True,
        'calendario_data': calendario_data,
    }

    return render(request, 'core/calendario_grupo.html', context)


# def calendario_individual(request):

#     if request.method == 'POST':
#         # Instanciamos un formulario con datos
#         formulario = AltaEventoForm(request.POST)
#                 # Validarlo
#         if formulario.is_valid():
#             # Dar de alta la info
#             messages.info(request, "Evento cargado con éxito")
#             return redirect(reverse('index'))
#     else:   #GET
#         formulario = AltaEventoForm()

#     context = {
#         'add_event_form': formulario
#     }
#     return render(request, 'core/calendario_individual.html', context)


def integrante_estado(request, estado):
    return HttpResponse(f'Filtrar alumnos por estado: {estado}')


def cargar_horario(request):
    if request.method == 'POST':
        form = HorarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = HorarioForm()

    return render(request, 'core/cargar_horario.html', {'form': form})



class EventoListView(ListView):
    model = Evento
    context_object_name = 'event_list'
    template_name = 'core/calendario_individual.html'


class PersonaCreateView(CreateView):
    model = Persona
    template_name = 'core/alta_persona.html'
    success_url = 'listado'
    fields = '__all__'


class PersonaListView(ListView):
    model = Persona
    context_object_name = 'listado_personas'
    template_name = 'core/personas_listado.html'
