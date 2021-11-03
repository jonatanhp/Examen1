
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from .serializers import ProductoSerializer
from .models import Producto

# Create your views here.

class ListProductos(ListAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class CreateProducto(CreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class UpdateProducto(UpdateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class deleteProducto(DestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
