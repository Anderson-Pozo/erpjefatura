from django.urls import path
from .views import ListaContribuyente, CrearContribuyente

urlpatterns = [
    path('', ListaContribuyente.as_view(), name='lista_contribuyentes'),
    path('crear_contribuyente/', CrearContribuyente.as_view(), name='crear_contribuyente')
]

# URL Implicit views
urlpatterns += [

]
