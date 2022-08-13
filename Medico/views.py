from django.shortcuts import render, redirect
from .models import Medico
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Q

def MedicoView(request):
    return render(request,"medico/newMedico.html")

def RegistroMedicoView(request):
    dni = request.POST['dniMed']
    nom = request.POST['nombMed']
    apP = request.POST['apellPaMed']
    apM = request.POST['apellMaMed']
    nCol = request.POST['ColMMed']

    medico = Medico.objects.create(
        dni = dni,
        nombre = nom,
        apPat = apP,
        apMat = apM,
        nColMed = nCol
    )
    messages.success(request,'Medico registrado!')
    return redirect("/medico/nuevo/")


def busquedaMedico (request):
    if request.method == 'POST':

        searched = request.POST['searched'] #mismo nombre del html
        medicos = Medico.objects.filter(
            Q(dni__contains=searched) | Q(apPat__contains=searched) | Q(apMat__contains=searched) )
        return render(request,"medico/busquedaMed.html",
        {'searched':searched,'medicos':medicos})
    
    else:
        return render(request,"medico/busquedaMed.html",{})

def edicionMedicoView(request,dni):
    medico = Medico.objects.get(dni=dni)
    return render(request, "medico/edicionMedico.html",{"medico": medico})
    
def editarMedicoView(request):

    dni = request.POST['dniMed']
    nom = request.POST['nombMed']
    apP = request.POST['apellPaMed']
    apM = request.POST['apellMaMed']
    nCol = request.POST['colMMed']
    
    medico = Medico.objects.get(dni=dni)
    
    medico.nombre = nom
    medico.apPat = apP
    medico.apMat = apM   
    medico.nColMed = nCol

    medico.save()
    messages.success(request, 'Medico Actualizado')
    return redirect ('/medico/busquedaMedico')



def eliminarMedico(request, dni):
    medico = Medico.objects.get(dni=dni)
    medico.delete()

    messages.success(request, "medico eliminado!")
    return redirect('/medico/busquedaMedico')
