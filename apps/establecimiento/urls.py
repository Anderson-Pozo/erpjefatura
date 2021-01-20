from django.urls import path
from .views import ListaEstablecimiento, CrearEstablecimiento

urlpatterns = [
    path('', ListaEstablecimiento.as_view(), name='lista_establecimientos'),
    path('crear_establecimiento/', CrearEstablecimiento.as_view(), name='crear_establecimiento')
]

