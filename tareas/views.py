from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from .models import Proyecto, Tarea
from .forms import ProyectoForm, TareaForm


# Muestra únicamente los proyectos del usuario autenticado
class ListaProyectosView(LoginRequiredMixin, ListView):
    model = Proyecto
    template_name = 'tareas/lista_proyectos.html'
    context_object_name = 'proyectos'

    def get_queryset(self):
        return Proyecto.objects.filter(
            usuario=self.request.user
        )


# Crea un proyecto y lo asocia al usuario que inició sesión
@login_required
def crear_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)

        if form.is_valid():
            proyecto = form.save(commit=False)
            proyecto.usuario = request.user
            proyecto.save()

            return redirect('lista_proyectos')
    else:
        form = ProyectoForm()

    return render(
        request,
        'tareas/form_proyecto.html',
        {'form': form}
    )


# Registra un nuevo usuario y automáticamente inicia su sesión
def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            usuario = form.save()
            login(request, usuario)

            return redirect('lista_proyectos')
    else:
        form = UserCreationForm()

    return render(
        request,
        'registration/registro.html',
        {'form': form}
    )


# Permite editar solamente proyectos del usuario autenticado
@login_required
def editar_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(
        Proyecto,
        id=proyecto_id,
        usuario=request.user
    )

    if request.method == 'POST':
        form = ProyectoForm(
            request.POST,
            instance=proyecto
        )

        if form.is_valid():
            form.save()

            return redirect('lista_proyectos')
    else:
        form = ProyectoForm(instance=proyecto)

    return render(
        request,
        'tareas/form_proyecto.html',
        {
            'form': form,
            'titulo': 'Editar proyecto'
        }
    )


# Elimina solamente proyectos pertenecientes al usuario autenticado
@login_required
def eliminar_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(
        Proyecto,
        id=proyecto_id,
        usuario=request.user
    )

    if request.method == 'POST':
        proyecto.delete()

        return redirect('lista_proyectos')

    return render(
        request,
        'tareas/confirmar_eliminar_proyecto.html',
        {'proyecto': proyecto}
    )


# Muestra un proyecto y todas sus tareas asociadas
@login_required
def detalle_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(
        Proyecto,
        id=proyecto_id,
        usuario=request.user
    )

    tareas = Tarea.objects.filter(
        proyecto=proyecto
    )

    return render(
        request,
        'tareas/detalle_proyecto.html',
        {
            'proyecto': proyecto,
            'tareas': tareas
        }
    )


# Crea una nueva tarea asociada al proyecto seleccionado
@login_required
def crear_tarea(request, proyecto_id):
    proyecto = get_object_or_404(
        Proyecto,
        id=proyecto_id,
        usuario=request.user
    )

    if request.method == 'POST':
        form = TareaForm(request.POST)

        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.proyecto = proyecto
            tarea.save()

            return redirect(
                'detalle_proyecto',
                proyecto_id=proyecto.id
            )
    else:
        form = TareaForm()

    return render(
        request,
        'tareas/form_tarea.html',
        {
            'form': form,
            'proyecto': proyecto
        }
    )


# Permite editar solamente tareas pertenecientes al usuario autenticado
@login_required
def editar_tarea(request, tarea_id):
    tarea = get_object_or_404(
        Tarea,
        id=tarea_id,
        proyecto__usuario=request.user
    )

    if request.method == 'POST':
        form = TareaForm(
            request.POST,
            instance=tarea
        )

        if form.is_valid():
            form.save()

            return redirect(
                'detalle_proyecto',
                proyecto_id=tarea.proyecto.id
            )
    else:
        form = TareaForm(instance=tarea)

    return render(
        request,
        'tareas/form_tarea.html',
        {
            'form': form,
            'proyecto': tarea.proyecto
        }
    )


# Elimina solamente tareas pertenecientes al usuario autenticado
@login_required
def eliminar_tarea(request, tarea_id):
    tarea = get_object_or_404(
        Tarea,
        id=tarea_id,
        proyecto__usuario=request.user
    )

    proyecto_id = tarea.proyecto.id

    if request.method == 'POST':
        tarea.delete()

        return redirect(
            'detalle_proyecto',
            proyecto_id=proyecto_id
        )

    return render(
        request,
        'tareas/confirmar_eliminar_tarea.html',
        {
            'tarea': tarea,
            'proyecto': tarea.proyecto
        }
    )