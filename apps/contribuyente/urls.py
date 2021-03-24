from django.urls import path
from .views import *

urlpatterns = [
    path('natural/',
         ListaContribuyenteNatural.as_view(),
         name='lista_contribuyente_natural'
         ),
    path('natural/crear/',
         CrearContribuyenteNatural.as_view(),
         name='crear_contribuyente_natural'
         ),
    path('natural/editar/<int:pk>/',
         EditarContribuyenteNatural.as_view(),
         name='editar_contribuyente_natural'
         ),
    path('natural/eliminar/<int:pk>/',
         EliminarContribuyenteNatural.as_view(),
         name='eliminar_contribuyente_natural'
         )
]

# URL Juridico
urlpatterns += [
    path('juridico/',
         ListaContribuyenteJuridico.as_view(),
         name='lista_contribuyente_juridico'
         ),
    path('juridico/crear/',
         CrearContribuyenteJuridico.as_view(),
         name='crear_contribuyente_juridico'
         ),
    path('juridico/editar/<int:pk>/',
         EditarContribuyenteJuridico.as_view(),
         name='editar_contribuyente_juridico'
         ),
    path('juridico/eliminar/<int:pk>/',
         EliminarContribuyenteJuridico.as_view(),
         name='eliminar_contribuyente_juridico'
         )
]
