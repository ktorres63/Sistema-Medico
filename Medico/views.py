from django.shortcuts import render
from django.views.generic import ListView

class MedicoListView(ListView):
    model = Medico
    template_name = 'pruebaMedicos.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_date(**kwargs)
        context['titulo'] = 'Medicos'
        return context