from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('contacto/', views.contacto, name='contacto'),
    path('eventos/alta', views.alta_evento, name='eventos_alta'),
    path('personas/alta', views.alta_persona, name='personas_alta'),
    path('personas/listado', views.PersonaListView.as_view(), name='personas_listado'),
    path('personas/calendario', views.EventoListView.as_view(), name='calendario_individual'),
    path('grupos/alta', views.GrupoCreateView.as_view(), name='grupos_alta'),
    path('grupos/listado', views.GrupoListView.as_view(), name='grupos_listado'),
    path('grupos/detalle/<int:id_grupo>', views.grupo_detalle, name='grupos_detalle'),
    path('grupos/update/<int:pk>/', views.GrupoUpdateView.as_view(), name='grupos_modificar'),
    path('grupos/delete/<int:pk>/', views.GrupoDeleteView.as_view(), name='grupos_eliminar'),
    path('tiempos-libres/<int:persona_id>/', views.visualizar_tiempos_libres, name='tiempos_libres'),
]
