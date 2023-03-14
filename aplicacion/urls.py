from django.urls import path
from aplicacion.views import *


urlpatterns = [
    path('index/', index, name="index"),
    path('Crear_curso/', Crear_curso, name="Crear_curso"),
    path('Crear_estudiante/', Crear_estudiante, name="Crear_estudiante"),
    path('Crear_profesor/', Crear_profesor, name="Crear_profesor"),
    path('busqueda/', busqueda, name="busqueda"),
    path('buscar/', buscar, name="buscar"),
    path('resultadobusqueda/', resultadobusqueda, name="resultadobusqueda"),
    path('Error_busqueda/', Error_busqueda, name="Error_busqueda"),
    

]