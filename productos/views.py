from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import Producto,Categorias
from productos.forms import ProductoForm,AgregaProducto
# Create your views here.

#Muestra los productos filtrados que contengan el nombre.
def productos(request):

    if 'search' in request.GET:
        search=request.GET['search']
        total_productos=Producto.objects.filter(nombre__icontains=search)
    else:
        total_productos=Producto.objects.all()

    return render(request,'productos/productos.html',{'total_productos':total_productos})


#AGREGA PRODUCTOS NUEVOS
def agregar_producto(request):
    context={
        'form':AgregaProducto
    }

    if request.method == 'POST':
        formulario=AgregaProducto(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            context['mensaje'] = 'Agregado correctamente'
        else:
            context['form']=formulario

    return render(request,'productos/agregar.html',context)


#MUESTRA UNA LISTA DE TODOS LOS PRODUCTOS
def listar_productos(request):
    productos=Producto.objects.all()
    context={
        'productos':productos
    }
    return render(request, 'productos/listar.html',context)



#ACTUALIZA EL PRODUCTO
def modificar_producto(request,id):
    producto = Producto.objects.get(id=id)

    if request.method == 'GET':
        context = {
            'form': ProductoForm(
                initial={
                    'nombre':producto.nombre,
                    'precio':producto.precio,
                    'stock':producto.stock,

                    }
                )
            }
    
    elif request.method == 'POST':
        formulario=ProductoForm(request.POST)

        if formulario.is_valid():
                producto.nombre= formulario.cleaned_data['nombre']
                producto.precio= formulario.cleaned_data['precio']
                producto.stock= formulario.cleaned_data['stock']
                producto.save()
            
                context={
                    'message':'Actualizado correctamente'
                }
        else:
            context={
                'form_errors':formulario.errors,
                'form':ProductoForm
            }


    return render(request,'productos/modificar.html',context)


def eliminar_producto(request, id):
    producto=get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect(to='listar-producto')