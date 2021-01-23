from django.urls import path, re_path
from .views import ListaCatastro, CrearContribuyente

urlpatterns = [
    path('lista_catastro/', ListaCatastro.as_view(), name='lista_catastro'),
    path('crear_contribuyente/', CrearContribuyente.as_view(), name='crear_contribuyente')
    # path('crear_patente/', CrearPatente.as_view(), name='crear_patente')
]