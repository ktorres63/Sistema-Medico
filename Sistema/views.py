from django.shortcuts import render,redirect
from django.views.generic import ListView
from .models import *

def loginView(request):
    return render(request,"login.html")

def HomeView(request):
    return render(request,"home.html")
