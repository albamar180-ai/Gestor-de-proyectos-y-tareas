from django.contrib import admin
from .models import Proyecto, Tarea


# Personalización del modelo Proyecto en el panel de administración
@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    # Columnas visibles en el listado de proyectos
    list_display = (
        'nombre',
        'usuario',
        'fecha_creacion'
    )

    # Permite buscar proyectos por nombre o usuario
    search_fields = (
        'nombre',
        'usuario__username'
    )

    # Permite filtrar los proyectos por fecha de creación
    list_filter = (
        'fecha_creacion',
    )

    # Muestra primero los proyectos más recientes
    ordering = (
        '-fecha_creacion',
    )


# Personalización del modelo Tarea en el panel de administración
@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    # Columnas visibles en el listado de tareas
    list_display = (
        'titulo',
        'proyecto',
        'completada',
        'fecha_creacion'
    )

    # Permite buscar tareas por título o nombre del proyecto
    search_fields = (
        'titulo',
        'proyecto__nombre'
    )

    # Permite filtrar por estado y fecha de creación
    list_filter = (
        'completada',
        'fecha_creacion'
    )

    # Muestra primero las tareas más recientes
    ordering = (
        '-fecha_creacion',
    )