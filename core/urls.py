from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('grupos/listado/', views.gestion_grupos, name='Gestion de grupos'),
    path('grupos/detalle/<str:nombre_alumno>/', views.grupo_detalle, name='Calendario individual'),
    path('grupos/historico/2017/', views.calendario_grupo, name='Calendario de grupo'),
    path('grupos/historico/', views.calendario_grupo, name='Calendario de grupo'),  # Ruta adicional para historico
    path('cargar_horario/', views.cargar_horario, name='cargar_horario'),
    path('grupos/activos/', views.integrante_estado, {'estado': 'activo'}, name="integrantes activos"),
    path('grupos/inactivos/', views.integrante_estado, {'estado': 'inactivo'}, name="integrantes inactivos"),
]
