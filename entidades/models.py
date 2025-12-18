from django.db import models
from django.contrib.auth.models import User

# Modelo de negocio de la Aplicacion
class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField()
    profesor = models.ForeignKey('Profesor', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"
        ordering = ["apellido", "-nombre"]

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Entregable(models.Model):
    nombre = models.CharField(max_length=50)
    fechaEntrega = models.DateField()
    entregado = models.BooleanField()

    def __str__(self): 
        return f"{self.nombre} - Entregado: {self.entregado}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png', null=True, blank=True)

    def __str__(self):
        return f"Profile {self.user.username}"