from django.urls import path
from .views import GetDirecciones

urlpatterns = [
    path('get_direcciones/', GetDirecciones.as_view(), name='get_direcciones'),
]
