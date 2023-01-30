from django.db import models

# Create your models here.

class Categorias(models.Model):
    nombre=models.CharField(max_length=50)

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'
    
    def __str__(self):
        return self.nombre
    

class Producto(models.Model):
    nombre=models.CharField(max_length=100)
    precio=models.FloatField()
    stock=models.BooleanField(default=True)
    imagen=models.ImageField(upload_to='productos',null=True,blank=True)

    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'
    
    def __str__(self):
        return self.nombre