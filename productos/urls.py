from django.urls import path
from productos import views


urlpatterns = [
    path('',views.productos,name='productos'),
    path('crear-productos/',views.crear_productos,name='crear-productos'),
    path('crear-categorias/',views.crear_categorias,name='crear-categorias'),
    path('categorias/',views.categorias,name='categorias'),
]