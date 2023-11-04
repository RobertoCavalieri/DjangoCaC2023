from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacto/', views.contacto, name='contacto'),

    path('eventos/alta', views.alta_evento, name='eventos_alta'),
    path('personas/alta', views.PersonaCreateView.as_view(), name='personas_alta'),
    path('personas/listado', views.PersonaListView.as_view(), name='personas_listado'),
    path('personas/calendario', views.EventoListView.as_view(), name='calendario_individual'),
    # path('grupos/listado', views.GrupoListView, name='grupos_listado'),
    # path('grupos/calendario', views.calendario_grupo, name='Calendario de grupo'),
    # path('cargar_horario', views.cargar_horario, name='cargar_horario'),

]