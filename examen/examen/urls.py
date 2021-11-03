"""examen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework import routers
from productosApp.views import ListProductos,CreateProducto,UpdateProducto,deleteProducto
from productosApp import views

router = routers.DefaultRouter()

router.register('productos', views.ListProductos)
router.register('productos/crear', views.CreateProducto)
router.register('productos/editar/<int:pk>/', views.UpdateProducto)
router.register('productos/eliminar/<int:pk>/', views.deleteProducto)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/productos/',include("productosApp.urls")),
    path('productos',ListProductos.as_view(),name='listarrr'),
    path('productos/crear',CreateProducto.as_view(),name='crearrr'),
    path('productos/editar/<int:pk>/',UpdateProducto.as_view(),name='actualizarrr'),
    path('productos/eliminar/<int:pk>/',deleteProducto.as_view(),name='eliminarrr')
]
