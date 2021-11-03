from django.urls import path
from productosApp import views

urlpatterns = [
    path("",views.ListProductos.as_view(),name="listar_productos"),
    path("create/", views.CreateProducto.as_view(),name="crear_productos"),
    path("update/<int:pk>/",views.UpdateProducto.as_view(),name="actualizar_productos"),
    path("delete/<int:pk>/",views.deleteProducto.as_view(),name="eliminar_productos")
]