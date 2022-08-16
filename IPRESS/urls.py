from django.urls import path
from IPRESS.views import *

urlpatterns =[
    path('nuevo/',IPRESSView, name='Nuevo_IPRESS'),
    path('nuevo/registro/',RegistroIPRESSView, name='registro'),
    path('editarIPRESS/', editarIPRESSView, name='editarIPRESS'),
    path('busquedaIPRESS/', busquedaIPRESS , name='busquedaIPRESS'),
    path('busquedaIPRESS/edicionIPRESS/<cod>',edicionIPRESSView, name='edicionIPRESS'),
    path('busquedaIPRESS/eliminarIPRESS/<cod>', eliminarIPRESS, name='eliminarIPRESS'),

]