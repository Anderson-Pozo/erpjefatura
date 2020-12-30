from django.urls import path, re_path
from .views import ListaVencimiento

urlpatterns = [
    path('listado_vencimiento/', ListaVencimiento.as_view(), name='listado_vencimiento')
]
