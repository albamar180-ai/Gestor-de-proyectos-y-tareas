from django.db import models
from django.contrib.auth.models import User


# Modelo que representa los proyectos creados por cada usuario
class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    # Relaciona cada proyecto con un usuario de Django
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='proyectos'
    )

    fecha_creacion = models.DateTimeField(auto_now_add=True)

    # Define cómo se mostrará el proyecto en Django Admin
    def __str__(self):
        return self.nombre


# Modelo que representa las tareas asociadas a un proyecto
class Tarea(models.Model):

    # Relación entre una tarea y su proyecto
    proyecto = models.ForeignKey(
        Proyecto,
        on_delete=models.CASCADE,
        related_name='tareas'
    )

    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    completada = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    # Define cómo se mostrará la tarea en Django Admin
    def __str__(self):
        return self.titulo