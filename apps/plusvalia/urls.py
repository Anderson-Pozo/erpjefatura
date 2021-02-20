from django.urls import path
from .views import CrearPlusvalia, ListaPlusvalia

urlpatterns = [
    path('', ListaPlusvalia.as_view(), name='lista_plusvalia'),
    path('crear_plusvalia/', CrearPlusvalia.as_view(), name='crear_plusvalia')
]
