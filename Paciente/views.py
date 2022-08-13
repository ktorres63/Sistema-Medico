from django.shortcuts import render, redirect
from .models import Paciente
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Q


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
    messages.success(request,'Paciente registrado!')
    return redirect("/paciente/nuevo")


def PacienteView(request):
    return render(request,"paciente/newPacient.html")

#------Receta Farmacia, FUA, hoja SIS
def recetaFarmaciaView(request):

    if request.method == 'POST':
        searched = request.POST['searched'] #mismo nombre del html
        pacientes = Paciente.objects.filter(dni__contains=searched)
        
        return render(request,"paciente/recFarmBusqueda.html",
        {'searched':searched,'pacientes':pacientes})
    
    else:
        return render(request,"paciente/recFarmBusqueda.html",{})
#-------------------
def edicionPacienteView(request,dni):
    paciente = Paciente.objects.get(dni=dni)
    return render(request, "paciente/edicionPaciente.html",{"paciente": paciente})

def editarPacienteView(request):

    dni = request.POST['dniPac']
    nom = request.POST['nombPac']
    apP = request.POST['apellPaPac']
    apM = request.POST['apellMaPac']
    telf = request.POST['telfPac']
    edad = request.POST['edPac']
    dir = request.POST['dirPac']
    fecNa = request.POST['nacPac']
    
    paciente = Paciente.objects.get(dni=dni)
    
    paciente.nombre = nom
    paciente.apPat = apP
    paciente.apMat = apM   
    paciente.telf = telf
    paciente.edad = edad
    paciente.dir = dir
    paciente.fechNac = fecNa

    paciente.save()

    messages.success(request, 'Paciente Actualizado')
    return redirect ('/paciente/busquedaPaciente')
   
def busquedaPaciente (request):
    if request.method == 'POST':

        searched = request.POST['searched'] #mismo nombre del html
        pacientes = Paciente.objects.filter(
            Q(dni__contains=searched) | Q(apPat__contains=searched) | Q(apMat__contains=searched) )
        return render(request,"paciente/busquedaPac.html",
        {'searched':searched,'pacientes':pacientes})
    
    else:
        return render(request,"paciente/busquedaPac.html",{})

def eliminarPaciente(request, dni):
    paciente = Paciente.objects.get(dni=dni)
    paciente.delete()

    messages.success(request, "Curso eliminado!")
    return redirect('/paciente/busquedaPaciente')

def formatosView(request, dni):
    paciente = Paciente.objects.get(dni=dni)

    return render(
        request,
        "paciente/formatos.html",
        {"paciente":paciente})