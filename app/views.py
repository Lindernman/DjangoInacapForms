import random
from django.shortcuts import redirect, render
from django.http import HttpResponse
from app.models import Persona
from django.views import generic
comunas = ['Puente Alto', 'Santiago', 'Macul',
           'Providencia', 'Maipo', 'Buin', 'Nunork']


def inicio(request):
    return render(request, 'index.html')









