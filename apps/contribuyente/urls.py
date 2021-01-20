from django.urls import path
from .views import ListaContribuyenteNatural, \
    CrearContribuyenteNatural, \
    ListaContribuyenteJuridico, \
    CrearContribuyenteJuridico, \
    EditarContribuyenteNatural

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
         )
]

# URL Implicit views
urlpatterns += [
    path('juridico/',
         ListaContribuyenteJuridico.as_view(),
         name='lista_contribuyente_juridico'
         ),
    path('juridico/crear/',
         CrearContribuyenteJuridico.as_view(),
         name='crear_contribuyente_juridico'
         )
]
