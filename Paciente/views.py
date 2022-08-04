from django.shortcuts import render, redirect
from .models import Paciente

def RegistroPacienteView(request):
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
    return redirect("/paciente/nuevo")


def PacienteView(request):
    return render(request,"paciente/newPacient.html")
