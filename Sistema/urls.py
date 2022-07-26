from django.urls import path
from Sistema.views import *

urlpatterns = [
    path('',loginView, name='login'),
    path('Medicos/',MedicoListView.as_view(), name='gestion_Medicos')

]
