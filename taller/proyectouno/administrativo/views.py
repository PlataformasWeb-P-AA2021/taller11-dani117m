from django.shortcuts import render, redirect
from django.http import HttpResponse

# importar las clases de models.py
from administrativo.models import *

# importar las clases de models.py
from administrativo.forms import*


def index(request):
    """
        Listar los registros del modelo Estudiante,
        obtenidos de la base de datos.
    """
    # a través del ORM de django se obtiene
    # los registros de la entidad; el listado obtenido
    # se lo almacena en una variable llamada
    # estudiantes
    edificio = Edificio.objects.all()
    # en la variable tipo diccionario llamada informacion_template
    # se agregará la información que estará disponible
    # en el template
    informacion_template = {'edificios': edificio, 'index_edificios': len(edificio)}
    return render(request, 'index.html', informacion_template)



def obtener_edificio(request, id):
    """
        Listar los registros del modelo Estudiante,
        obtenidos de la base de datos.
    """
    # a través del ORM de django se obtiene
    # los registros de la entidad; el listado obtenido
    # se lo almacena en una variable llamada
    # estudiantes
    edificio = Edificio.objects.get(pk=id)
    # en la variable tipo diccionario llamada informacion_template
    # se agregará la información que estará disponible
    # en el template
    informacion_template = {'edificio': edificio}
    return render(request, 'obtener_edificio.html', informacion_template)


def crear_edificio(request):
    """
    """
    if request.method=='POST':
        formulario = edificioForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() # se guarda en la base de datos
            return redirect(index)
    else:
        formulario = edificioForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crear_edificio.html', diccionario)

def editar_edificio(request, id):
    """
    """
    edificio = Edificio.objects.get(pk=id)
    if request.method=='POST':
        formulario = edificioForm(request.POST, instance=edificio)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = edificioForm(instance=edificio)
    diccionario = {'formulario': formulario}

    return render(request, 'editar_edificio.html', diccionario)


def eliminar_edificio(request, id):
    """
    """
    edificio = Edificio.objects.get(pk=id)
    edificio.delete()
    return redirect(index)

#####################################
def crear_Departamento(request):
    """
    """

    if request.method=='POST':
        formulario = DepartamentoForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = DepartamentoForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crear_Departamento.html', diccionario)


def editar_Departamentoo(request, id):
    """
    """
    departamento = Departamento.objects.get(pk=id)
    if request.method=='POST':
        formulario = DepartamentoForm(request.POST, instance=departamento)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = DepartamentoForm(instance=departamento)
    diccionario = {'formulario': formulario}

    return render(request, 'crear_Departamento.html', diccionario)

def crear_numero_Departamento(request, id):
    """
    """
    edificio = Edificio.objects.get(pk=id)
    if request.method=='POST':
        formulario = NumeroDepartamentoForm(edificio, request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = NumeroDepartamentoForm(edificio)
    diccionario = {'formulario': formulario, 'edificio': edificio}

    return render(request, 'crearNumero_Departamento.html', diccionario)
