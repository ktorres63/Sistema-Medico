from django.shortcuts import render,redirect
from django.views.generic import ListView
from .models import *

def loginView(request):
    return render(request,"login.html")

def formatos(request):
    return render(request,"formatos.html")

def HomeView(request):
    return render(request,"home.html")

def NuevoPac(request):
    return render(request,"newPacient.html")

def registrarPaciente(request):
    dni = request.POST['dniPac']
    nom = request.POST['nombPac']
    apP = request.POST['apellPaPac']
    apM = request.POST['apellMaPac']
    telf = request.POST['telfPac']
    edad = request.POST['edPac']
    dir = request.POST['dirPac']
    fecNa = request.POST['nacPac']

    paciente = Paciente.objects.create(
        dni = dni,
        nombre = nom,
        apPat = apP,
        apMat = apM,
        telf = telf,
        edad = edad,
        dir = dir,
        fechNac = fecNa
    )
    return redirect("/home")


class MedicoListView(ListView):
    model = Medico
    template_name = 'pruebaMedicos.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_date(**kwargs)
        context['titulo'] = 'Medicos'
        return context
