from django.urls import path
from .views import CrearAlcabala, ListaAlcabala, GetPersonas

urlpatterns = [
    path('', ListaAlcabala.as_view(), name='lista_alcabala'),
    path('crear_alcabala/', CrearAlcabala.as_view(), name='crear_alcabala'),
    path('get_personas/', GetPersonas.as_view(), name='get_personas')
]
