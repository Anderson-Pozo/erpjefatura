from django.urls import path
from .views import CrearAlcabala

urlpatterns = [
    path('crear_alcabala/', CrearAlcabala.as_view(), name='crear_alcabala')
]
