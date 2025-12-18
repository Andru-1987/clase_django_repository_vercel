from django.contrib import admin
from .models import *
# Register your models here.

class CursoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "comision", "profesor")
    list_filter = ("comision",)

class ProfesorAdmin(admin.ModelAdmin):
    list_display = ("apellido", "nombre", "email", "profesion")

admin.site.register(Curso, CursoAdmin)
admin.site.register(Profesor, ProfesorAdmin)    
admin.site.register(Estudiante)    
admin.site.register(Entregable)    
admin.site.register(Profile)    
