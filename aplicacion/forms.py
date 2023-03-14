from django import forms

class CrearCurso(forms.Form):
    nombre = forms.CharField(max_length=30)
    camada = forms.IntegerField()

class CrearEstudiante(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()

class CrearProfesor(forms.Form):

    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=30)