from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.views.generic import ListView, CreateView


from datetime import datetime

# from core.forms import AltaEventoForm
from core.forms import EventoForm
from core.forms import ContactoForm
from core.models import Evento
from core.models import Persona

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


def alta_evento(request):
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