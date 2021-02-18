from django.urls import path
from .views import CrearPlusvalia

urlpatterns = [
    path('crear_plusvalia/', CrearPlusvalia.as_view(), name='crear_plusvalia')
]
