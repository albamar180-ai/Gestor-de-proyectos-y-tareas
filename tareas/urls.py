from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListaProyectosView.as_view(), name='lista_proyectos'),
    path('proyectos/nuevo/', views.crear_proyecto, name='crear_proyecto'),
    path('registro/', views.registro, name='registro'),
    path('proyectos/<int:proyecto_id>/editar/', views.editar_proyecto, name='editar_proyecto'),
    path('proyectos/<int:proyecto_id>/eliminar/', views.eliminar_proyecto, name='eliminar_proyecto'),
    path('proyectos/<int:proyecto_id>/', views.detalle_proyecto, name='detalle_proyecto'),
    path('proyectos/<int:proyecto_id>/tareas/nueva/', views.crear_tarea, name='crear_tarea'),
    path('tareas/<int:tarea_id>/editar/', views.editar_tarea, name='editar_tarea'),
    path('tareas/<int:tarea_id>/eliminar/', views.eliminar_tarea, name='eliminar_tarea'),
]