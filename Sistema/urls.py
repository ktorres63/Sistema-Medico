from django.urls import path
from Sistema.views import *

urlpatterns = [
    path('',loginView, name='login'),
    #path('Medicos/',MedicoListView.as_view(), name='gestion_Medicos'),
    path('home/',HomeView, name='home'),
    #path('pacienteNuevo/',NuevoPac, name='nuevoP'),
    #path('pacienteNuevo/registroPaciente/',registrarPaciente, name='PacR'),
    path('formatos',formatosView, name='formatos'),
]
