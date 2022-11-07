


### **1.- Clonar repositorio**
https://github.com/Lindernman/DjangoInacapForms

### **2.- Verificar?**
### **3.- Crear ruta personas**
```py
# urls.py
path('personas', views.personas, name='personas'),

# views.py
def personas(request):
    personas = Persona.objects.values()
    return render(request, 'personas.html', {'personas': personas})
```
***
### **3.1- Crear plantilla**
```html
<!-- crear personas.html -->
{% extends "base.html" %}

{% block content %}

<div class="flex gap-4 justify-center w-full max-w-4xl mx-auto p-10">
    <div class="bg-slate-500">
        Registro
    </div>
    <div class="bg-slate-500">
        Usuarios
    </div>
</div>

{% endblock content %}
```
***
### **4.- Crear ruta para registrar usuario**
```py
# views.py
def registrar(request):

    Persona.objects.create(nombre=request.POST['nombre'], edad=random.randint(
        18, 99), comuna=random.choice(comunas))
    return redirect('personas')
# urls.py
path('personas/registrar', views.registrar, name='registrar'),

```


### **4.1- Agregar formulario de registro de usuario**
Que es el CSRF TOKEN y para que sirve:

El CSRF Token permite prevenir ataque por falsificasion de solicitudes, por codigos de 3eros
```html
<!-- personas.html -->
<form class="flex flex-col gap-2 my-2" type="submit" method="POST" action="{% url 'registrar' %}">
    {% csrf_token %}
    <input required name="nombre" class="input" type="text" placeholder="Ingrese el nombre">
    <button class="btn btn-success btn-sm">Registrar</button>
</form>
```
***
### **5- Agregar tabla para visualizar usuarios**
```html
<!-- personas.html -->
<div class="overflow-x-auto">
    <table class="table table-zebra w-full table-compact font-bold">

        <thead>
            <tr>
                <th>ID</th>
                <th>Nombre</th>

                <th>Accion</th>
            </tr>
        </thead>
        <tbody>
            {% for persona in personas  %}
            <tr>
                <td>{{persona.id}}</td>
                <td>{{persona.nombre}}</td>
                <td>Accion</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</div>

```
***
### **6.- Crear la ruta/url de detalle de la persona**
Que recibe un parametro como una llave primaria la cual se usara para consultar la base de datos, en este caso seria el ID

```py
# urls.py
path('personas/<id>', views.detalle, name='detalle'),

# views.py
def detalle(request, id):

    persona = Persona.objects.get(id=id)
    return render(request, 'detalle.html', {'persona': persona})

```
***
### **6.1- Template del detalle**

```html
<!-- Crear detalle.html -->
{% extends "base.html" %}
{% block content %}
<div class="flex items-center justify-center flex-col  max-w-xl mx-auto mt-10 gap-2">


    <div class="font-extrabold text-xl">
        Detalle Persona
    </div>
    <div class="overflow-x-auto p-2  w-full max-w-md">
        <table class="table table-zebra w-full table-compact font-bold">
            <tbody>
                <tr>
                    <td>ID</td>
                    <td>{{persona.id}}</td>
                </tr>
                <tr class="w-full">
                    <td> Nombre</td>
                    <td>
                        <div id="nombre">{{persona.nombre}}</div>
                    </td>
                </tr>
                <tr>
                    <td>Edad</td>
                    <td>{{persona.edad}}</td>
                </tr>
                <tr>
                    <td>Comuna</td>
                    <td>{{persona.comuna}}</td>
                </tr>
            </tbody>
        </table>
    </div>

</div>



{% endblock content %}
<!-- Agregar el boton en personas.html la columna de acciones. -->
 <td><a href="/personas/{{persona.id}}" class="btn btn-xs ">Detalle</a></td>
```
***
### **7.- Crear ruta para eliminar a la persona por su ID**

```py
#  urls.py
path('personas/<id>/eliminar', views.eliminar, name='eliminar'),

# views.py
def eliminar(request, id):
    Persona.objects.get(id=id).delete()
    return redirect('personas')
```
***
### **7.1- Crear ruta para eliminar a la persona por su ID**

```html
<!-- Agregar el formulario despues del div que cierra la tabla -->
<!-- detalle.html -->
<form class="mt-2" type="submit" action="{% url 'eliminar' persona.id %}" method="POST">
    {% csrf_token %}
    <button class="btn btn-sm btn-warning"> Eliminar</button>
</form>
```
***
### **8.- Crear ruta para actualizar a la persona por su ID**
```py
#  urls.py
path('personas/<int:id>/actualizar', views.actualizar, name='actualizar'),

# views.py
def actualizar(request, id):

    Persona.objects.filter(id=id).update(
        nombre=request.POST['nombre'])
    return redirect('detalle', id)
```
***
### **8.1 - Agregar el boton para editar y la logica de este**
```html
<!-- detalle.html -->
<!-- Agregar boton para editar el nombre del usuario con el evento de click -->
<button onclick="editarUsuario()" class="btn btn-xs text-sm">Editar</button>

<!-- Antes de cerrar el bloque de contenido -->
<template id="template">

    <form class="mt-2" type="submit" action="{% url 'actualizar' persona.id  %}" method="POST"
        class="flex gap-2">
        {% csrf_token %}
        <input type="text" name="nombre" value="{{persona.nombre}}" class="input input-sm bg-slate-500 w-32">
        <button class="btn btn-sm btn-warning"> Guardar</button>
    </form>

</template>

<script>
    let nombre = document.getElementById('nombre')
    let template = document.getElementById('template')

    function editarUsuario(event) {
        nombre.replaceWith(template.content)
    }
</script>
```
***
### **9.- Explicar vistas genericas**
 Son consultas basicas a la base de datos, como traer una lista o datos filtrados por algun parametro de la url se pueden abreviar con las "VISTAS GENERICAS
Las vistas genericas abstraen patrones comunas que permiten escribir menos codigo

NOTA: Cambiar el id a pk

```py
# views.py

class PersonasView(generic.ListView):
    context_object_name = 'personas'
    model = Persona
    template_name = 'personas.html'
    
class DetalleView(generic.DetailView):
    model = Persona
    template_name = 'detalle.html'


# Rutas de urls.py
path('personas', views.PersonasView.as_view(), name='personas'),
# NOTA: Cambiar el id a pk ya que nececita identificar la llave primaria
path('personas/<pk>', views.DetalleView.as_view(), name='detalle'),

```

FIN