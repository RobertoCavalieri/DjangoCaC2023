from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('evento', views.evento, name='evento'),
    path('grupos/listado/', views.gestion_grupos, name='Gestion de grupos'),
    path('grupos/detalle/', views.EventoListView.as_view(), name='calendario_individual'),
    path('grupos/calendario/', views.calendario_grupo, name='Calendario de grupo'),
    path('cargar_horario/', views.cargar_horario, name='cargar_horario'),
]
