from django.urls import path
from productos import views


urlpatterns = [
    path('',views.productos,name='productos'),
    path('agregar-producto/',views.agregar_producto,name='agregar-producto'),
    path('listar-producto/',views.listar_productos,name='listar-producto'),
    path('modificar-producto/<int:id>/',views.modificar_producto,name='modificar-producto'),
    path('eliminar-producto/<id>/',views.eliminar_producto,name='eliminar-producto'),
]