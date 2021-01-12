from django.urls import path
from .views import ListaContribuyente

urlpatterns = [
    path('', ListaContribuyente.as_view(), name='lista_contribuyentes'),
]

# URL Implicit views
urlpatterns += [

]
