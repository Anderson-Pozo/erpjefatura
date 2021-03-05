from django.urls import path
from .views import Index, Calendario

urlpatterns = [
    path('index_contribuyente/', Index.as_view(), name='index_contribuyente'),
    path('calendario/', Calendario.as_view(), name='calendario'),
]
