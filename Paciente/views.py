from django.shortcuts import render, redirect
from .models import Paciente
from django.http import HttpResponse

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

def formatosView(request):
    return render(request,"paciente/formatos.html")

def busqueda(request):
    if request.method == 'POST':
        searched = request.POST['searched'] #mismo nombre del html
        pacientes = Paciente.objects.filter(dni__contains=searched)
        print(pacientes)
        return render(request,"paciente/busqueda.html",
        {'searched':searched,'pacientes':pacientes})
    
    else:
        return render(request,"paciente/busqueda.html",{})


    
   

