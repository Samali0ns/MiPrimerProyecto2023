from django.urls import path
from . import views


urlpatterns = [
    
    path('',views.profile_user,name='profile_user'),
]