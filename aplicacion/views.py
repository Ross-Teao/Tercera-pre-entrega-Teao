from django.shortcuts import render
from django.http import HttpResponse
from aplicacion.models import Curso,Estudiante, Profesor
from aplicacion.forms import CrearCurso,CrearEstudiante, CrearProfesor

# Create your views here.

######################################## INDEX ########################################

def index(request):
    
    return render(request,"aplicacion/index.html")

######################################## CREAR CURSO ########################################

def Crear_curso(request):
    
    if request.method == "POST":
        
        miformulario = CrearCurso(request.POST)
        print(miformulario)
        
        if miformulario.is_valid:
            informacion = miformulario.cleaned_data
            curso = Curso(nombre=informacion["nombre"], camada=informacion["camada"])
        
            curso.save()

            return render(request, "aplicacion/index.html")
        
    else:
    
        miformulario = CrearCurso()
        
    return render(request, "aplicacion/Crear_curso.html", {"miformulario":miformulario})

######################################## CREAR ESTUDIANTE ########################################

def Crear_estudiante(request):
    
    if request.method == "POST":
        
        miformulario = CrearEstudiante(request.POST)
        print(miformulario)
        
        if miformulario.is_valid:
            informacion = miformulario.cleaned_data
            curso = Estudiante(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"])
        
            curso.save()
            return render(request, "aplicacion/index.html")
        
    else:
    
        miformulario = CrearEstudiante()
        
    return render(request, "aplicacion/Crear_estudiante.html", {"miformulario":miformulario})

######################################## CREAR PROFESOR ########################################

def Crear_profesor(request):
    
    if request.method == "POST":
        
        miformulario = CrearProfesor(request.POST)
        print(miformulario)
        
        if miformulario.is_valid:
            informacion = miformulario.cleaned_data
            curso = Profesor(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"], profesion=informacion["profesion"])
        
            curso.save()
            return render(request, "aplicacion/index.html")
        
    else:
    
        miformulario = CrearProfesor()
        
    return render(request, "aplicacion/Crear_profesor.html", {"miformulario":miformulario})


######################################## BUSQUEDA CAMADA ########################################

def busqueda(request):

     return render(request, "aplicacion/buscar.html")
 
 
def Error_busqueda(request):
    
    return render(request,"aplicacion/Error_busqueda.html")

 ######################################## BUSQUEDA CAMADA ########################################
 
def buscar(request):

     if request.GET['camada']:
         camada = request.GET['camada']
         cursos = Curso.objects.filter(camada__icontains=camada)

         return render(request, "aplicacion/resultadobusqueda.html",{"cursos":cursos, "camada":camada})

     else:

         respuesta = render(request, "aplicacion/Error_busqueda.html")

     return HttpResponse(respuesta)
 
######################################## BUSQUEDA CAMADA ########################################
  
def resultadobusqueda(request):

     return render(request, "aplicacion/resultadobusqueda.html")