from django import forms
from .models import Proyecto, Tarea


# Formulario utilizado para crear y editar proyectos
class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre', 'descripcion']

    # Valida que el nombre tenga al menos 3 caracteres
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre'].strip()

        if len(nombre) < 3:
            raise forms.ValidationError(
                'El nombre del proyecto debe tener al menos 3 caracteres.'
            )

        return nombre


# Formulario utilizado para crear y editar tareas
class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'completada']

    # Valida que el título tenga al menos 3 caracteres
    def clean_titulo(self):
        titulo = self.cleaned_data['titulo'].strip()

        if len(titulo) < 3:
            raise forms.ValidationError(
                'El título de la tarea debe tener al menos 3 caracteres.'
            )

        return titulo