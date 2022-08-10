from django.urls import path, include
from Sistema.views import *
from . import views

urlpatterns = [
    path('',loginView, name='login'),
    #path('Medicos/',MedicoListView.as_view(), name='gestion_Medicos'),
    path('home/',HomeView, name='home'),
    #path('pacienteNuevo/',NuevoPac, name='nuevoP'),
    #path('pacienteNuevo/registroPaciente/',registrarPaciente, name='PacR'),
    #path('formatos',formatosView, name='formatos'),
    path('salir/', views.salir, name="salir"),
]
