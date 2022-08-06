from django.urls import path
from Paciente.views import *

urlpatterns =[
    path('nuevo/',PacienteView, name='Nuevo_Paciente'),
    path('nuevo/registro/',RegistroPacienteView, name='registro'),
    path('nuevo/formatos/',formatosView, name='formatos'),
    path('busqueda/', busqueda, name='busqueda')

]
