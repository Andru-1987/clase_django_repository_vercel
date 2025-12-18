from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth import authenticate

# Create your views here.
def home(request):
    return render(request, "entidades/index.html")

@login_required 
def cursos(request):
    contexto = {"cursos": Curso.objects.all()}
    return render(request, "entidades/cursos.html", contexto)

@login_required 
def profesores(request):
    contexto = {"profesores": Profesor.objects.all()}
    return render(request, "entidades/profesores.html", contexto)

@login_required 
def estudiantes(request):
    contexto = {"estudiantes": Estudiante.objects.all()}
    return render(request, "entidades/estudiantes.html", contexto)

@login_required 
def entregables(request):
    contexto = {"entregables": Entregable.objects.all()}
    return render(request, "entidades/entregables.html", contexto)

@login_required 
def cursoForm(request):
    if request.method == "POST":
        miFormulario = CursoForm(request.POST) # Aqui me llega toda la informacion del formulario
        if miFormulario.is_valid():
            curso_nombre = miFormulario.cleaned_data.get("nombre")
            curso_comision = miFormulario.cleaned_data.get("comision")
            curso_profesor = miFormulario.cleaned_data.get("profesor")
            curso = Curso(nombre=curso_nombre, comision=curso_comision, profesor=curso_profesor)
            curso.save()
            contexto = {"cursos": Curso.objects.all()}
            return render(request, "entidades/cursos.html", contexto)
    else:
        # Es la primer vez que se ingresa al formulario
        # Se crea un formulario vacío
        miFormulario = CursoForm()

    contexto = { "form": miFormulario}
    return render(request, "entidades/cursoForm.html", contexto)

@login_required 
def cursoUpdate(request, id):
    curso = Curso.objects.get(id=id)

    if request.method == "POST":
        miFormulario = CursoForm(request.POST) # Aqui me llega toda la informacion del formulario
        if miFormulario.is_valid():
            curso.nombre = miFormulario.cleaned_data.get("nombre")
            curso.comision = miFormulario.cleaned_data.get("comision")            
            curso.profesor = miFormulario.cleaned_data.get("profesor")            
            curso.save()
            contexto = {"cursos": Curso.objects.all()}
            return render(request, "entidades/cursos.html", contexto)
    else:
        # Es la primer vez que se ingresa al formulario
        # Se crea un formulario vacío
        miFormulario = CursoForm(initial={"nombre": curso.nombre, "comision": curso.comision})

    contexto = { "form": miFormulario}
    return render(request, "entidades/cursoForm.html", contexto)

@login_required 
def cursoDelete(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    contexto = {"cursos": Curso.objects.all()}
    return render(request, "entidades/cursos.html", contexto)

# Profesores

@login_required 
def profesorForm(request):
    if request.method == "POST":
        miFormulario = ProfesorForm(request.POST) # Aqui me llega toda la informacion del formulario
        if miFormulario.is_valid():
            profesor_nombre = miFormulario.cleaned_data.get("nombre")
            profesor_apellido = miFormulario.cleaned_data.get("apellido")
            profesor_email = miFormulario.cleaned_data.get("email")
            profesor_profesion = miFormulario.cleaned_data.get("profesion")
            profesor = Profesor(nombre=profesor_nombre, apellido=profesor_apellido, email=profesor_email, profesion=profesor_profesion)
            profesor.save()
            contexto = {"profesores": Profesor.objects.all()}
            return render(request, "entidades/profesores.html", contexto)
    else:
        # Es la primer vez que se ingresa al formulario
        # Se crea un formulario vacío
        miFormulario = ProfesorForm()

    contexto = { "form": miFormulario}
    return render(request, "entidades/profesorForm.html", contexto)

@login_required 
def profesorUpdate(request, id):
    profesor = Profesor.objects.get(id=id)

    if request.method == "POST":
        miFormulario = ProfesorForm(request.POST) # Aqui me llega toda la informacion del formulario
        if miFormulario.is_valid():
            profesor.nombre = miFormulario.cleaned_data.get("nombre")
            profesor.apellido = miFormulario.cleaned_data.get("apellido")            
            profesor.email = miFormulario.cleaned_data.get("email")            
            profesor.profesion = miFormulario.cleaned_data.get("profesion")            
            profesor.save()
            contexto = {"profesores": Profesor.objects.all()}
            return render(request, "entidades/profesores.html", contexto)
    else:
        # Es la primer vez que se ingresa al formulario
        # Se crea un formulario vacío
        miFormulario = ProfesorForm(initial={"nombre": profesor.nombre, "apellido": profesor.apellido, "email": profesor.email, "profesion": profesor.profesion})

    contexto = { "form": miFormulario}
    return render(request, "entidades/profesorForm.html", contexto)

@login_required 
def profesorDelete(request, id):
    profesor = Profesor.objects.get(id=id)
    profesor.delete()
    contexto = {"profesores": Profesor.objects.all()}
    return render(request, "entidades/profesores.html", contexto)

#___________________ Estudiantes
#  Usar Classes Based Views para la gestion de Estudiantes

class EstudianteListView(LoginRequiredMixin, ListView):
    model = Estudiante
    template_name = "entidades/estudiante_registros.html"

    # Opcional: modificar el contexto para enviar datos adicionales
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['estudiante_list'] = Estudiante.objects.all()
        #context['estudiante_list'] = Estudiante.objects.filter(nombre__icontains='P')
        return context

class EstudianteCreateView(LoginRequiredMixin, CreateView):
    model = Estudiante
    fields = [ 'nombre', 'apellido', 'email']
    success_url = reverse_lazy('estudiantes')

class EstudianteUpdateView(LoginRequiredMixin, UpdateView):
    model = Estudiante
    fields = [ 'nombre', 'apellido', 'email']
    success_url = reverse_lazy('estudiantes')

class EstudianteDeleteView(LoginRequiredMixin, DeleteView):
    model = Estudiante
    success_url = reverse_lazy('estudiantes')


# __________________ Buscar Curso
@login_required 
def buscarCursos(request):
    return render(request, "entidades/buscarCursos.html")

@login_required 
def encontrarCursos(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        cursos = Curso.objects.filter(nombre__icontains=patron)
        contexto = {"cursos": cursos, "patron": patron}
        return render(request, "entidades/cursos.html", contexto)
    else:
        respuesta = "No se ingresó ningún dato de búsqueda."
        return render(request, "entidades/cursos.html", {"respuesta": respuesta})

# __________________ Login / Logout / Registration
#     

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    #fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')
    
def register(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')   
    else:
        form = RegistroForm()
    return render(request, 'registration/register.html', {'form': form})     

@login_required 
def perfil(request):
    usuario = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirige a la página de perfil después de guardar
    else:
        form = ProfileForm(instance=usuario)

    return render(request, 'registration/perfil.html', {'form': form} )  


@login_required 
def avatar(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AvatarForm(instance=profile)
    return render(request, 'registration/avatar.html', {'form': form})