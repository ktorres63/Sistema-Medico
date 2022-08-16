from django.shortcuts import render, redirect
from .models import IPRESS
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Q

def IPRESSView(request):
    return render(request,"ipress/newIPRESS.html")

def RegistroIPRESSView(request):
    cod = request.POST['codIPRESS']
    nom = request.POST['nombIPRESS']
    tipSeg = request.POST['tipSegIPRESS']

    ipress = IPRESS.objects.create(
        cod = cod,
        nombre = nom,
        tipSeg = tipSeg,
    )
    messages.success(request,'IPRESS registrado!')
    return redirect("/ipress/nuevo/")

def busquedaIPRESS (request):
    if request.method == 'POST':

        searched = request.POST['searched'] #mismo nombre del html
        ipress = IPRESS.objects.filter(
            Q(cod__contains=searched) | Q(nombre__contains=searched) )
        return render(request,"ipress/busquedaIPRESS.html",
        {'searched':searched,'ipress':ipress})
    
    else:
        return render(request,"ipress/busquedaIPRESS.html",{})

def edicionIPRESSView(request,cod):
    ipress = IPRESS.objects.get(cod=cod)
    return render(request, "ipress/edicionIPRESS.html",{"ipress": ipress})

def editarIPRESSView(request):

    cod = request.POST['codIPRESS']
    nom = request.POST['nombIPRESS']
    tipSeg = request.POST['tipSegIPRESS']
    
    ipress = IPRESS.objects.get(cod=cod)
    
    ipress.nombre = nom
    ipress.tipSeg = tipSeg

    ipress.save()
    messages.success(request, 'IPRESS Actualizado')
    return redirect ('/ipress/busquedaIPRESS')

def eliminarIPRESS(request, cod):
    ipress = IPRESS.objects.get(cod=cod)
    ipress.delete()

    messages.success(request, "IPRESS eliminado!")
    return redirect('/ipress/busquedaIPRESS')