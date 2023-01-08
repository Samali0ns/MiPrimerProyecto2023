from django.shortcuts import render,HttpResponse
from .models import Producto,Categorias
from productos.forms import ProductoForm
# Create your views here.

#Crea desde admin y la web y valida productos (la importacion de imagen la deje solo para admin)
def crear_productos(request):
    if request.method == 'GET':
        contexto={
                'form':ProductoForm()
                }
        return render(request,'productos/crear_productos.html',context=contexto)
    
    elif request.method == 'POST':
        formulario=ProductoForm(request.POST)

        if formulario.is_valid():
            Producto.objects.create(
                    nombre=formulario.cleaned_data['nombre'],
                    precio=formulario.cleaned_data['precio'],
                    stock=formulario.cleaned_data['stock'],
                    )
            contexto={
                'mensaje':"Producto creado exitosamente"
            }
            return render(request,'productos/crear_productos.html',context=contexto)
        
        else:
            contexto={
                'formulario_errores':formulario.errors,
                'form':ProductoForm()
            }
            return render(request,'productos/crear_productos.html',context=contexto)


#Crea Categorias desde el admin o desde el link
def crear_categorias(request):
    Categorias.objects.create(nombre='Blancas')
    return HttpResponse("Categoria Creada")


#Muestra los productos filtrados que contengan el nombre.
def productos(request):

    if 'search' in request.GET:
        search=request.GET['search']
        total_productos=Producto.objects.filter(nombre__icontains=search)
    else:
        total_productos=Producto.objects.all()

    return render(request,'productos/productos.html',{'total_productos':total_productos})


def categorias(request):
    total_categorias=Categorias.objects.all()
    return render(request,'productos/categorias.html',{'categorias':total_categorias})