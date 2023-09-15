from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


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
    return render(request, 'core/grupo_detalle.html', context)


def calendario_grupo(request, year):
    context = {
        'year': year,
    }
    return render(request, 'core/calendario_grupo.html', context)


def calendario_individual(request):
    return render(request, 'core/cargar_horario.html')


def integrante_estado(request, estado):
    return HttpResponse(f'Filtrar alumnos por estado: {estado}')


def cargar_horario(request):
    return render(request, 'core/cargar_horario.html')
