from django.db import models

# Create your models here.
class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30, verbose_name="O Endereco")
    email = models.EmailField(blank=True, null=True)
    tfno = models.CharField(max_length=10)
    
    def __str__(self):
        return self.nombre
    
class Articulos(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=30)
    precio = models.IntegerField()
    
    def __str__(self):
        return 'El nombre es %s, la sección es %s y el precio es %s' %(self.nombre, self.seccion, self.precio)
    
class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()