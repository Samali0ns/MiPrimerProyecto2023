from django.shortcuts import render

# Create your views here.

def sobremi(request):
    return render(request,'sobremi/sobremi.html')