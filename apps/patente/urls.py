from django.urls import path, re_path
from .views import ListaCatastro

urlpatterns = [
    path('lista_catastro/', ListaCatastro.as_view(), name='lista_catastro')
]