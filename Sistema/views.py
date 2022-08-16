from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import ListView, View
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from Medico.models import *
from IPRESS.models import *
from Paciente.models import *




@login_required
def loginView(request):
    return render(request,"home.html")

def salir(request):
    logout(request)
    return redirect('/')

def HomeView(request):
    return render(request,"home.html")

class ListaEmpleadosListView(ListView):
    model = Paciente
    template_name = "formatos/receta.html"
    context_object_name = "paciente"

'''class recetaPDF(View):
    def get(self, request, *args, **kwargs):
        pacientes = Paciente.object.get(dni=DNI)
        medicos = Medico.objecto.get(dni=123456789)

        data = {
            "medico" : medicos.dni
        }
        pdf = render_to_pdf("formatos/receta.html", data)
        return HttpResponse(pdf, content_type="application/pdf")'''