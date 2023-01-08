from django.contrib import admin
from .models import Producto,Categorias
# Register your models here.

#Mostramos desde el admin nombre,precio y stock de los productos y filtros
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display=('nombre','precio','stock')
    list_filter=('stock',)
    search_fields=('nombre',)



admin.site.register(Categorias)
