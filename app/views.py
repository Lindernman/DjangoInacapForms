from django.shortcuts import redirect, render

import random
from django.http import HttpResponse
from app.models import Persona
from django.views import generic
comunas = ['Puente Alto', 'Santiago', 'Macul',
           'Providencia', 'Maipo', 'Buin', 'Nunork']


def inicio(request):
    return render(request, 'index.html')


# def personas(request):

#     personas = Persona.objects.values()
#     return render(request, 'personas.html', {'personas': personas})


def registrar(request):

    Persona.objects.create(nombre=request.POST['nombre'], edad=random.randint(
        18, 99), comuna=random.choice(comunas))
    return redirect('personas')


# def detalle(request, id):

#     persona = Persona.objects.get(id=id)
#     return render(request, 'detalle.html', {'persona': persona})


def eliminar(request, id):
    Persona.objects.get(id=id).delete()
    return redirect('personas')


def actualizar(request, id):

    Persona.objects.filter(id=id).update(
        nombre=request.POST['nombre'])
    return redirect('detalle', id)

# def personas(request):

#     personas = Persona.objects.values()
#     return render(request, 'personas.html', {'personas': personas})


class PersonasView(generic.ListView):
    context_object_name = 'personas'
    model = Persona
    template_name = 'personas.html'
    
class DetalleView(generic.DetailView):
    model = Persona
    template_name = 'detalle.html'
    

    # def get_queryset(self):
    #     """Return the last five published questions."""
    #     return Question.objects.order_by('-pub_date')[:5]
