from django.urls import path
from .views import HomeContribuyente, ListaContribuyente

urlpatterns = [
    path('lista_contribuyentes/', ListaContribuyente.as_view(), name='lista_contribuyentes'),
]

# URL Implicit views
urlpatterns += [
    path('', HomeContribuyente.as_view(), name='home'),
]
