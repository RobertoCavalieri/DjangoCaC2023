
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime

from core.forms import HorarioForm


def index(request):
    context = {
        'nombre_usuario': 'Jose Lopez',
        'fecha': datetime.now(),
        'es_instructor': True,
    }
    return render(request, "core/index.html", context)


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


def calendario_individual(request):
    context = {
        'nombre_usuario': 'Jose Lopez',
        'fecha': datetime.now(),
    }
    return render(request, 'core/calendario_individual.html', context)



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
