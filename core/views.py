from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime

from core.forms import HorarioForm


def index(request):
    context = {
        'nombre_usuario': 'Carlos Perez',
        'fecha': datetime.now(),
        'es_instructor': True,
    }
    return render(request, "core/index.html", context)


def gestion_grupos(request):
    # Esta data en el futuro vendrá de la base de datos
    listado = [
        'Carlos Lopez',
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
        'nombre_usuario': 'Carlos Perez',
        'fecha': datetime.now(),
        'es_instructor': True,
        'calendario_data': calendario_data,
    }
    # Resto de la lógica de la vista

    return render(request, 'core/calendario_grupo.html', context)


def calendario_individual(request):
    context = {
        'nombre_integrante': 'Jose Lopez',
    }
    return render(request, 'core/calendario_individual.html')


def integrante_estado(request, estado):
    return HttpResponse(f'Filtrar alumnos por estado: {estado}')


def cargar_horario(request):
    if request.method == 'POST':
        form = HorarioForm(request.POST)
        if form.is_valid():
            form.save()  # Esto guardará el horario en la base de datos
            return redirect('index')  # Redireccionar a la página principal u otra página

    else:
        form = HorarioForm()

    return render(request, 'core/cargar_horario.html', {'form': form})
