from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('grupos/listado/', views.gestion_grupos, name='Gestion de grupos'),
    path('grupos/detalle/<str:nombre_integrante>/', views.calendario_individual, name='Calendario individual'),
    path('grupos/calendario/', views.calendario_grupo, name='Calendario de grupo'),
    path('cargar_horario/', views.cargar_horario, name='cargar_horario'),
]
