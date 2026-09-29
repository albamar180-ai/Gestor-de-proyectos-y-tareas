from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from .models import Proyecto, Tarea


class ProyectoTareaTestCase(TestCase):

    def setUp(self):
        self.usuario = User.objects.create_user(
            username='usuario_prueba',
            password='clave12345'
        )

        self.proyecto = Proyecto.objects.create(
            nombre='Proyecto de prueba',
            descripcion='Descripción del proyecto',
            usuario=self.usuario
        )

    def test_crear_proyecto(self):
        self.assertEqual(
            self.proyecto.nombre,
            'Proyecto de prueba'
        )
        self.assertEqual(
            self.proyecto.usuario,
            self.usuario
        )

    def test_crear_tarea(self):
        tarea = Tarea.objects.create(
            proyecto=self.proyecto,
            titulo='Tarea de prueba',
            descripcion='Descripción de la tarea'
        )

        self.assertEqual(tarea.titulo, 'Tarea de prueba')
        self.assertEqual(tarea.proyecto, self.proyecto)
        self.assertFalse(tarea.completada)

    def test_lista_proyectos_requiere_login(self):
        respuesta = self.client.get(
            reverse('lista_proyectos')
        )

        self.assertEqual(respuesta.status_code, 302)

    def test_usuario_autenticado_accede_a_proyectos(self):
        self.client.login(
            username='usuario_prueba',
            password='clave12345'
        )

        respuesta = self.client.get(
            reverse('lista_proyectos')
        )

        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(
            respuesta,
            'Proyecto de prueba'
        )
        
    def test_crear_proyecto_desde_vista(self):
        self.client.login(
            username='usuario_prueba',
            password='clave12345'
        )

        respuesta = self.client.post(
            reverse('crear_proyecto'),
            {
                'nombre': 'Nuevo proyecto',
                'descripcion': 'Proyecto creado desde una prueba'
            }
        )

        self.assertEqual(respuesta.status_code, 302)

        self.assertTrue(
            Proyecto.objects.filter(
                nombre='Nuevo proyecto',
                usuario=self.usuario
            ).exists()
        )
    def test_editar_proyecto_desde_vista(self):
        self.client.login(
            username='usuario_prueba',
            password='clave12345'
        )

        respuesta = self.client.post(
            reverse(
                'editar_proyecto',
                args=[self.proyecto.id]
            ),
            {
                'nombre': 'Proyecto actualizado',
                'descripcion': 'Descripción modificada'
            }
        )

        self.assertEqual(respuesta.status_code, 302)

        self.proyecto.refresh_from_db()

        self.assertEqual(
            self.proyecto.nombre,
            'Proyecto actualizado'
        )
        
    def test_eliminar_proyecto_desde_vista(self):
        self.client.login(
            username='usuario_prueba',
            password='clave12345'
        )

        respuesta = self.client.post(
            reverse(
                'eliminar_proyecto',
                args=[self.proyecto.id]
            )
        )

        self.assertEqual(respuesta.status_code, 302)

        self.assertFalse(
            Proyecto.objects.filter(
                id=self.proyecto.id
            ).exists()
        )
        
    def test_crear_tarea_desde_vista(self):
        self.client.login(
            username='usuario_prueba',
            password='clave12345'
        )

        respuesta = self.client.post(
            reverse(
                'crear_tarea',
                args=[self.proyecto.id]
            ),
            {
                'titulo': 'Nueva tarea',
                'descripcion': 'Tarea creada desde una prueba',
                'completada': False
            }
        )

        self.assertEqual(respuesta.status_code, 302)

        self.assertTrue(
            Tarea.objects.filter(
                titulo='Nueva tarea',
                proyecto=self.proyecto
            ).exists()
        )
        
    def test_editar_tarea_desde_vista(self):
        tarea = Tarea.objects.create(
            proyecto=self.proyecto,
            titulo='Tarea original',
            descripcion='Descripción original'
        )

        self.client.login(
            username='usuario_prueba',
            password='clave12345'
        )

        respuesta = self.client.post(
            reverse(
                'editar_tarea',
                args=[tarea.id]
            ),
            {
                'titulo': 'Tarea actualizada',
                'descripcion': 'Descripción modificada',
                'completada': True
            }
        )

        self.assertEqual(respuesta.status_code, 302)

        tarea.refresh_from_db()

        self.assertEqual(
            tarea.titulo,
            'Tarea actualizada'
        )

        self.assertTrue(tarea.completada)
        
    def test_eliminar_tarea_desde_vista(self):
        tarea = Tarea.objects.create(
            proyecto=self.proyecto,
            titulo='Tarea para eliminar',
            descripcion='Esta tarea será eliminada'
        )

        self.client.login(
            username='usuario_prueba',
            password='clave12345'
        )

        respuesta = self.client.post(
            reverse(
                'eliminar_tarea',
                args=[tarea.id]
            )
        )

        self.assertEqual(respuesta.status_code, 302)

        self.assertFalse(
            Tarea.objects.filter(
                id=tarea.id
            ).exists()
        )
        
        
        
        
