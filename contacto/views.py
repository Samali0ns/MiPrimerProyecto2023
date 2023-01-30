from django.shortcuts import render
from .forms import ContactoForm

# Create your views here.

def contacto(request):
    context={
        'form':ContactoForm
    }

    if request.method == 'POST':
        formulario=ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            context['mensaje'] = "Mensaje Enviado"
        else:
            context['form'] = formulario

    return render(request,'contacto/contacto.html',context)