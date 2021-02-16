from django.urls import path, re_path
from .views import ListaCatastro, CrearContribuyente, \
    CrearNatural, CrearJuridico, CrearEstablecimiento, CrearPatente, \
    ReportDeclaracion

urlpatterns = [
    path('lista_catastro/', ListaCatastro.as_view(), name='lista_catastro'),
    path('crear_contribuyente/natural/', CrearNatural.as_view(), name='crear_natural'),
    path('crear_contribuyente/juridico/', CrearJuridico.as_view(), name='crear_juridico'),
    path('crear_establecimiento/', CrearEstablecimiento.as_view(), name='crear_establecimiento'),
    path('crear_patente/', CrearPatente.as_view(), name='crear_patente'),
    path('report_declaracion/<int:pk>/', ReportDeclaracion.as_view(), name='report_declaracion')
]
