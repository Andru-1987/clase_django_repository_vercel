from django.test import TestCase
from entidades.models import Estudiante


class TestMessage(TestCase):

    def test_hello_world(self):
        self.assertEqual("hello world", "hello world")



class EstudianteModelTest(TestCase):
    
    def setUp(self):
        self.estudiante = Estudiante.objects.create(
            nombre="María",
            apellido="González",
            email="maria@example.com"
        )
    def test_estudiante_str(self):
        """Verifica el método __str__ del estudiante"""
        self.assertEqual(str(self.estudiante), "María González")
