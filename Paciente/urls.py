from django.urls import path
from Paciente.views import *

urlpatterns =[
    path('nuevo/',PacienteView, name='Nuevo_Paciente'),
    path('nuevo/registro/',RegistroPacienteView, name='registro'),
    path('editarPaciente/', editarPacienteView, name='editarPaciente'),
    path('busquedaPaciente/', busquedaPaciente, name='busquedaPac'),
    path('busquedaPaciente/edicionPaciente/<dni>',edicionPacienteView, name='edicionPaciente'),
    path('editarPaciente/', editarPacienteView, name='editarPaciente'),
    path('busquedaPaciente/eliminarPaciente/<dni>', eliminarPaciente, name='eliminarPaciente'),
    #receta Farmacia, FUA, hoja sis
    path('RFbusqueda/', recetaFarmaciaView, name='busquedaDoc'), #busqueda para el generar documento
    path('RFbusqueda/<int:dni>',formatosView, name='formatos'),




]
