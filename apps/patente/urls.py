from django.urls import path, re_path
from .views import ListaCatastro, CrearContribuyente, CrearEstablecimiento, CrearContribuyenteJuridico, CrearPatente

urlpatterns = [
    path('lista_catastro/', ListaCatastro.as_view(), name='lista_catastro'),
    path('crear_contribuyente/', CrearContribuyente.as_view(), name='crear_contribuyente'),
    path('crear_contribuyente_juridico/', CrearContribuyenteJuridico.as_view(), name='crear_contribuyente_juridico'),
    path('crear_establecimiento/', CrearEstablecimiento.as_view(), name='crear_establecimiento'),
    path('crear_patente/', CrearPatente.as_view(), name='crear_patente')
]