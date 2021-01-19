from django.urls import path, re_path
from .views import ListaVencimiento, ListaMulta, ListaImpuesto, CrearMulta

urlpatterns = [
    path('lista_vencimiento/', ListaVencimiento.as_view(), name='lista_vencimiento'),
    path('lista_multa/', ListaMulta.as_view(), name='lista_multa'),
    path('lista_impuesto/', ListaImpuesto.as_view(), name='lista_impuesto'),
    path('crear_multa/', CrearMulta.as_view(), name='crear_multa')
]
