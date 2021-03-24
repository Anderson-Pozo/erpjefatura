from django.urls import path
from .views import ListaEstablecimiento, CrearEstablecimiento, EditarEstablecimiento

urlpatterns = [
    path('', ListaEstablecimiento.as_view(), name='lista_establecimientos'),
    path('crear_establecimiento/', CrearEstablecimiento.as_view(), name='crear_establecimiento'),
    path('editar/<int:pk>/', EditarEstablecimiento.as_view(), name='editar_establecimiento'),
]
