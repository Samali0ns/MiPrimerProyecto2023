from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profileuser
from .forms import RegisterForm, UserUpdateForm,ProfileUpdateFrom


#INICIO DE SECION
def login_view(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {
            'form':form
        }
        return render(request, 'registro/login.html', context=context)
    
    elif request.method == 'POST':
        form = AuthenticationForm(request = request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                context = {
                    'message':f'Bienvenido {username}'
                }
                return render(request, 'ProyectoTiendaApp/home.html', context=context)

        form = AuthenticationForm()
        context ={
            'form':form,
            'errors':'Datos Incorrectos'
        }
        return render(request, 'registro/login.html', context=context)



#REGISTRO DE USUARIO
def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        context ={
            'form':form
        }
        return render(request, 'registro/register.html', context=context)

    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save() #al hacer el save, se crea el usuario
            Profileuser.objects.create(user=user)
            return redirect('login')
        
        context = {
            'errors':form.errors,
            'form':RegisterForm()
        }
        return render(request, 'registro/register.html', context=context)


#DEBE ESTAR LOGEADO PARA ACTUALIZAR SU PERFIL
@login_required
def update_user(request):
    user = request.user
    if request.method == 'GET':
        form = UserUpdateForm(initial = {
            'username':user.username,
            'first_name':user.first_name,
            'last_name':user.last_name
        })
        context ={
            'form':form
        }
        return render(request, 'registro/update_user.html', context=context)

    elif request.method == 'POST':
        form = UserUpdateForm(request.POST)
        if form.is_valid():
            user.username = form.cleaned_data.get('username')
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.save()
            return redirect('ProyectoTiendaApp/home')
        
        context = {
            'errors':form.errors,
            'form':RegisterForm()
        }
        return render(request, 'registro/update_user.html', context=context)


@login_required
def profile_user(request):
    return render(request,'registro/profile.html')


def update_profile(request):
    if request.method =='POST':

        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateFrom(
                request.POST,
                request.FILES,
                instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Perfil actualizado correctamente')
            return redirect('profile')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateFrom(instance=request.user.profile)

    context={
        'u_form':u_form,
        'p_form':p_form
    }

    return render(request,'registro/update_profile.html',context)
