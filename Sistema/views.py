from django.shortcuts import render
from django.views.generic import ListView
from .models import *

def loginView(request):
    return render(request,"login.html")

def HomeView(request):
    return render(request,"home.html")

def NuevoPac(request):
    return render(request,"newPacient.html")

class MedicoListView(ListView):
    model = Medico
    template_name = 'pruebaMedicos.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_date(**kwargs)
        context['titulo'] = 'Medicos'
        return context
