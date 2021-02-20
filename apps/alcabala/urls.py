from django.urls import path
from .views import CrearAlcabala, ListaAlcabala

urlpatterns = [
    path('', ListaAlcabala.as_view(), name='lista_alcabala'),
    path('crear_alcabala/', CrearAlcabala.as_view(), name='crear_alcabala')
]
