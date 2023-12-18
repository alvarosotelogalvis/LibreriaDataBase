from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Libro
from .forms import LibroForm

# Create your views here.
def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def libros(request):
    libros = Libro.objects.all()
    #print(libros)
    return render(request, 'libros/index.html', {'libros':libros})

#def crear(request):
#    formulario = LibroForm(request.POST or None, request.FILES or None)
#    print("CREAR")
#    if formulario.is_valid():
#        print("Creado")
#        formulario.save()
#        return redirect('libros')
#    else:
#        print("No Creado")
#   return render(request, 'libros/crear.html', {'formulario':formulario})

def crear(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if request.method=='GET':
        print("Enviando formulario.")
    else:
        print(request.POST)
        print("Obteniendo datos.")
    return render(request, 'libros/crear.html', {'formulario':formulario})

def editar(request, id):
    libro = Libro.objects.get(id=id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)
    #print("EDITAR")
    if formulario.is_valid() and request.POST:
        #print("editar")
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/editar.html', {'formulario':formulario})

def eliminar(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('libros')
    #return render(request, 'libros/eliminar.html')
