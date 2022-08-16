from django.urls import path, include
from Sistema.views import *
from . import views

urlpatterns = [
    path('',loginView, name='login'),
    path('home/',HomeView, name='home'),
    path('salir/', views.salir, name="salir"),
    #path("receta/", views.recetaPDF.as_view(), name="receta"),
]
