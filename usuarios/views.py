from django.shortcuts import render

# Create your views here.


def profile_user(request):
    return render(request,'usuarios/profile.html')