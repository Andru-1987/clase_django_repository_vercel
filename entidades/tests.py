from django.test import TestCase
from django.contrib.auth.models import User
from datetime import date
from .models import Curso, Estudiante, Profesor, Entregable, Profile


class CursoModelTest(TestCase):
    """Tests para el modelo Curso"""
    
    def setUp(self):
        """Configuración inicial para cada test"""
        self.profesor = Profesor.objects.create(
            nombre="Juan",
            apellido="Pérez",
            email="juan@example.com",
            profesion="Ingeniero"
        )
        self.curso = Curso.objects.create(
            nombre="Python Avanzado",
            comision=101,
            profesor=self.profesor
        )
    
    def test_curso_creation(self):
        """Verifica que el curso se crea correctamente"""
        self.assertEqual(self.curso.nombre, "Python Avanzado")
        self.assertEqual(self.curso.comision, 101)
        self.assertEqual(self.curso.profesor, self.profesor)
    
    def test_curso_str(self):
        """Verifica el método __str__ del curso"""
        self.assertEqual(str(self.curso), "Python Avanzado")
    
    def test_curso_sin_profesor(self):
        """Verifica que se puede crear un curso sin profesor"""
        curso_sin_profesor = Curso.objects.create(
            nombre="Django Básico",
            comision=102
        )
        self.assertIsNone(curso_sin_profesor.profesor)
    
    def test_delete_profesor_deletes_curso(self):
        """Verifica que al eliminar un profesor se eliminan sus cursos (CASCADE)"""
        curso_id = self.curso.id
        self.profesor.delete()
        with self.assertRaises(Curso.DoesNotExist):
            Curso.objects.get(id=curso_id)


class EstudianteModelTest(TestCase):
    """Tests para el modelo Estudiante"""
    
    def setUp(self):
        self.estudiante = Estudiante.objects.create(
            nombre="María",
            apellido="González",
            email="maria@example.com"
        )
    
    def test_estudiante_creation(self):
        """Verifica que el estudiante se crea correctamente"""
        self.assertEqual(self.estudiante.nombre, "María")
        self.assertEqual(self.estudiante.apellido, "González")
        self.assertEqual(self.estudiante.email, "maria@example.com")
    
    def test_estudiante_str(self):
        """Verifica el método __str__ del estudiante"""
        self.assertEqual(str(self.estudiante), "María González")
    
    def test_email_format(self):
        """Verifica que el email tiene un formato válido"""
        self.assertIn("@", self.estudiante.email)


class ProfesorModelTest(TestCase):
    """Tests para el modelo Profesor"""
    
    def setUp(self):
        self.profesor1 = Profesor.objects.create(
            nombre="Ana",
            apellido="Martínez",
            email="ana@example.com",
            profesion="Doctora en Ciencias"
        )
        self.profesor2 = Profesor.objects.create(
            nombre="Carlos",
            apellido="López",
            email="carlos@example.com",
            profesion="Ingeniero"
        )
    
    def test_profesor_creation(self):
        """Verifica que el profesor se crea correctamente"""
        self.assertEqual(self.profesor1.nombre, "Ana")
        self.assertEqual(self.profesor1.apellido, "Martínez")
        self.assertEqual(self.profesor1.email, "ana@example.com")
        self.assertEqual(self.profesor1.profesion, "Doctora en Ciencias")
    
    def test_profesor_str(self):
        """Verifica el método __str__ del profesor"""
        self.assertEqual(str(self.profesor1), "Ana Martínez")
    
    def test_profesor_ordering(self):
        """Verifica el ordenamiento de profesores (apellido ASC, nombre DESC)"""
        profesores = list(Profesor.objects.all())
        self.assertEqual(profesores[0].apellido, "López")
        self.assertEqual(profesores[1].apellido, "Martínez")
    
    def test_verbose_names(self):
        """Verifica los nombres verbose del modelo"""
        self.assertEqual(Profesor._meta.verbose_name, "Profesor")
        self.assertEqual(Profesor._meta.verbose_name_plural, "Profesores")


class EntregableModelTest(TestCase):
    """Tests para el modelo Entregable"""
    
    def setUp(self):
        self.entregable = Entregable.objects.create(
            nombre="Trabajo Práctico 1",
            fechaEntrega=date(2024, 12, 31),
            entregado=False
        )
    
    def test_entregable_creation(self):
        """Verifica que el entregable se crea correctamente"""
        self.assertEqual(self.entregable.nombre, "Trabajo Práctico 1")
        self.assertEqual(self.entregable.fechaEntrega, date(2024, 12, 31))
        self.assertFalse(self.entregable.entregado)
    
    def test_entregable_str(self):
        """Verifica el método __str__ del entregable"""
        self.assertEqual(str(self.entregable), "Trabajo Práctico 1 - Entregado: False")
    
    def test_entregable_entregado(self):
        """Verifica cambio de estado de entregado"""
        self.entregable.entregado = True
        self.entregable.save()
        entregable_actualizado = Entregable.objects.get(id=self.entregable.id)
        self.assertTrue(entregable_actualizado.entregado)


class ProfileModelTest(TestCase):
    """Tests para el modelo Profile"""
    
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123"
        )
        self.profile = Profile.objects.create(
            user=self.user
        )
    
    def test_profile_creation(self):
        """Verifica que el perfil se crea correctamente"""
        self.assertEqual(self.profile.user, self.user)
        self.assertEqual(self.profile.avatar, 'avatars/default.png')
    
    def test_profile_str(self):
        """Verifica el método __str__ del perfil"""
        self.assertEqual(str(self.profile), "Profile testuser")
    
    def test_profile_one_to_one_relationship(self):
        """Verifica la relación OneToOne con User"""
        self.assertEqual(self.user.profile, self.profile)
    
    def test_delete_user_deletes_profile(self):
        """Verifica que al eliminar un usuario se elimina su perfil (CASCADE)"""
        profile_id = self.profile.id
        self.user.delete()
        with self.assertRaises(Profile.DoesNotExist):
            Profile.objects.get(id=profile_id)
    
    def test_profile_unique_per_user(self):
        """Verifica que no se pueden crear múltiples perfiles para un usuario"""
        from django.db import IntegrityError
        with self.assertRaises(IntegrityError):
            Profile.objects.create(user=self.user)


class ModelIntegrationTest(TestCase):
    """Tests de integración entre modelos"""
    
    def setUp(self):
        self.profesor = Profesor.objects.create(
            nombre="Pedro",
            apellido="Sánchez",
            email="pedro@example.com",
            profesion="Licenciado"
        )
        self.curso = Curso.objects.create(
            nombre="Web Development",
            comision=201,
            profesor=self.profesor
        )
        self.estudiante = Estudiante.objects.create(
            nombre="Laura",
            apellido="Fernández",
            email="laura@example.com"
        )
    
    def test_profesor_tiene_cursos(self):
        """Verifica que se puede acceder a los cursos de un profesor"""
        cursos = self.profesor.curso_set.all()
        self.assertEqual(cursos.count(), 1)
        self.assertEqual(cursos.first(), self.curso)
    
    def test_multiple_cursos_mismo_profesor(self):
        """Verifica que un profesor puede tener múltiples cursos"""
        curso2 = Curso.objects.create(
            nombre="Mobile Development",
            comision=202,
            profesor=self.profesor
        )
        self.assertEqual(self.profesor.curso_set.count(), 2)