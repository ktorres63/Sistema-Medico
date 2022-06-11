from django.http import HttpResponse
from django.shortcuts import render

def MyHomeView(*args, **kwargs):
    return HttpResponse('<h1>  hola mundo </h1>')
