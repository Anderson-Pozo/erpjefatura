from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('lista_catastro/', ListaCatastro.as_view(), name='lista_catastro'),
    path('suspender/<int:pk>/', SuspenderPatente.as_view(), name='suspender'),
    path('editar/<int:pk>/', ExonerarPatente.as_view(), name='editar'),
    path('enviar_correo/<int:pk>/', EnviarCorreo.as_view(), name='enviar_correo'),

    path('crear_contribuyente/natural/', CrearNatural.as_view(), name='crear_natural'),
    path('crear_contribuyente/juridico/', CrearJuridico.as_view(), name='crear_juridico'),
    path('crear_establecimiento/', CrearEstablecimiento.as_view(), name='crear_establecimiento'),

    path('crear_patente/', CrearPatente.as_view(), name='crear_patente'),
    path('revision_declaracion/', RevisionDeclaracion.as_view(), name='revision_declaracion'),

    path('especie_patente/', CreacionEspecie.as_view(), name='especie_patente'),
    path('revision_especie/', RevisionEspecie.as_view(), name='revision_especie'),
]

# URL Renovar patente
urlpatterns += [
    path('renovacion/especie/<int:pk>', EspecieRenovacion.as_view(), name='especie_renovacion'),
    path('renovacion/revision/', RevisionEspModificada.as_view(), name='rev_especie'),
]

# URL Reportes
urlpatterns += [
    path('report_declaracion/<int:pk>/', ReportDeclaracion.as_view(), name='report_declaracion'),
    path('report_especie/<int:pk>/', ReportEspecie.as_view(), name='report_especie'),
]
