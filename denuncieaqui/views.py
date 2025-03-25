from django.shortcuts import render, redirect
from django.contrib import messages
from usuarios.models import CustomUser

def inicio(request):
    if request.method == "GET":
        return render(request, 'inicio.html')

def mapa(request):
    if request.method == "GET":
        return render(request, 'mapa.html')

def redirecionamento(request):
    if request.method == "GET":
        return render(request, 'redirecionamento.html')
    
def duvidas(request):
    if request.method == "GET":
        return render(request, 'duvidas.html')