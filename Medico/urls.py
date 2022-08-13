from django.urls import path
from Medico.views import *

urlpatterns =[
    path('nuevo/',MedicoView, name='Nuevo_Medico'),
    path('nuevo/registro/',RegistroMedicoView, name='registro'),
    path('editarMedico/', editarMedicoView, name='editarMedico'),
    path('busquedaMedico/', busquedaMedico , name='busquedaMed'),
    path('busquedaMedico/edicionMedico/<dni>',edicionMedicoView, name='edicionMedico'),
    path('busquedaMedico/eliminarMedico/<dni>', eliminarMedico, name='eliminarMedico'),

    
]
'''
    path('editarPaciente/', editarPacienteView, name='editarPaciente'),
    path('busquedaPaciente/', busquedaPaciente, name='busquedaPac'),
    path('busquedaPaciente/edicionPaciente/<dni>',edicionPacienteView, name='edicionPaciente'),
    path('editarPaciente/', editarPacienteView, name='editarPaciente'),
    path('busquedaPaciente/eliminarPaciente/<dni>', eliminarPaciente, name='eliminarPaciente'),
    #receta Farmacia, FUA, hoja sis
    path('RFbusqueda/', recetaFarmaciaView, name='busquedaDoc'), #busqueda para el generar documento
    path('RFbusqueda/<int:dni>',formatosView, name='formatos'), 
    '''