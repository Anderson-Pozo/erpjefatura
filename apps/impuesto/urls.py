from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('lista_vencimiento/', ListaVencimiento.as_view(), name='lista_vencimiento'),
    path('vencimiento/editar/<int:pk>/', EditarVencimiento.as_view(), name='editar_vencimiento'),

    path('lista_multa/', ListaMulta.as_view(), name='lista_multa'),
    path('crear_multa/', CrearMulta.as_view(), name='crear_multa'),
    path('multa/editar/<int:pk>/', EditarMulta.as_view(), name='editar_multa'),

    path('lista_impuesto/', ListaImpuesto.as_view(), name='lista_impuesto'),
    path('impuesto/editar/<int:pk>/', EditarImpuesto.as_view(), name='editar_impuesto'),
]
