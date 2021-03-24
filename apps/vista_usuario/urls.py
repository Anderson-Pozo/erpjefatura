from django.urls import path
from .views import Index, Calendario, Informacion

urlpatterns = [
    path('', Index.as_view(), name='index_consulta'),
    path('calendario/', Calendario.as_view(), name='calendario'),
    path('informacion/', Informacion.as_view(), name='informacion'),
]
