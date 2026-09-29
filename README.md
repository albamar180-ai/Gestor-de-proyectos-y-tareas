# Gestor de Proyectos y Tareas

Proyecto desarrollado en Django como parte del Módulo 6 del Bootcamp Full Stack Python.

La aplicación permite registrar usuarios y gestionar proyectos y tareas de forma independiente para cada usuario.

## Funcionalidades

- Registro de usuarios.
- Inicio y cierre de sesión.
- Creación de proyectos.
- Edición de proyectos.
- Eliminación de proyectos.
- Visualización de proyectos del usuario autenticado.
- Creación de tareas asociadas a proyectos.
- Edición de tareas.
- Eliminación de tareas.
- Estado de tareas completadas o pendientes.
- Validación de formularios.
- Restricción de acceso para usuarios no autenticados.
- Panel de administración de Django.
- Pruebas unitarias de modelos y vistas principales.

## Tecnologías utilizadas

- Python
- Django 5.2
- HTML
- CSS
- SQLite
- Django Templates

## Estructura principal

gestor_tareas/
- gestor_tareas/: configuración principal del proyecto.
- tareas/: aplicación encargada de proyectos y tareas.
- tareas/models.py: modelos Proyecto y Tarea.
- tareas/views.py: vistas y lógica de la aplicación.
- tareas/forms.py: formularios y validaciones.
- tareas/urls.py: rutas de la aplicación.
- tareas/admin.py: configuración del panel administrativo.
- tareas/tests.py: pruebas unitarias.
- templates/: plantillas HTML.
- manage.py: herramienta de administración de Django.
- db.sqlite3: base de datos SQLite.

## Instalación

1. Crear y activar un entorno virtual.

En Windows:

    python -m venv venv
    venv\Scripts\activate

2. Instalar Django 5.2:

    pip install Django==5.2

3. Aplicar las migraciones:

    python manage.py migrate

4. Crear un superusuario para acceder al administrador:

    python manage.py createsuperuser

5. Iniciar el servidor:

    python manage.py runserver

6. Abrir en el navegador:

    http://127.0.0.1:8000/

## Uso del sistema

Al ingresar a la aplicación, el usuario debe registrarse o iniciar sesión.

Una vez autenticado puede:

1. Crear un proyecto.
2. Editar o eliminar sus proyectos.
3. Ingresar a un proyecto para visualizar sus tareas.
4. Crear nuevas tareas.
5. Marcar tareas como completadas o pendientes.
6. Editar o eliminar tareas.
7. Cerrar sesión de forma segura.

Cada usuario puede acceder únicamente a sus propios proyectos y tareas.

## Panel de administración

Django proporciona un panel administrativo para gestionar los datos del sistema.

Se puede acceder mediante:

    http://127.0.0.1:8000/admin/

El administrador permite visualizar, buscar y filtrar proyectos y tareas.

## Validaciones y seguridad

La aplicación incluye:

- Protección CSRF en formularios.
- Restricción de acceso mediante autenticación.
- Uso de LoginRequiredMixin.
- Validaciones personalizadas en formularios.
- Asociación de proyectos al usuario autenticado.
- Restricción de acceso a proyectos y tareas pertenecientes a otros usuarios.

## Pruebas unitarias

Para ejecutar las pruebas:

    python manage.py test

El proyecto incluye pruebas para los modelos y vistas principales, incluyendo creación, edición y eliminación de proyectos y tareas, además de comprobaciones de autenticación y acceso.

Resultado obtenido durante el desarrollo:

    Ran 10 tests
    OK

## Autor

Alba Moreno

Bootcamp Full Stack Python  
Proyecto Módulo 6 - Django