from django.db import models

# Create your models here.
class Producto(models.Model):
    marca = models.CharField(max_length=100)
    serie = models.CharField(max_length=100)
    precio = models.FloatField()
    cantidad = models.IntegerField()
    disponible = models.IntegerField()
    descripcion = models.TextField()
    date_created = models.DateField(auto_created=True)
    last_modified = models.DateField(auto_now=True)
    

    def __str__(self):
        return self.marca
