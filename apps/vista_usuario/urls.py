from django.urls import path
from .views import Index, Calendario, Help

urlpatterns = [
    path('', Index.as_view(), name='index_contribuyente'),
    path('calendario/', Calendario.as_view(), name='calendario'),
    path('help/', Help.as_view(), name='help'),
]
