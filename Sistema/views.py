from django.shortcuts import render,redirect
from django.views.generic import ListView
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required
def loginView(request):
    return render(request,"home.html")

def salir(request):
    logout(request)
    return redirect('/')

def HomeView(request):
    return render(request,"home.html")
