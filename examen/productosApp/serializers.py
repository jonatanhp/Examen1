from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'marca', 'precio', 'serie','cantidad','disponible','descripcion','date_created']
        