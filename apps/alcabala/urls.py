from django.urls import path
from .views import CrearAlcabala, ListaAlcabala, GetPersonas, RevisionAlcabala, ReportAlcabala

urlpatterns = [
    path('', ListaAlcabala.as_view(), name='lista_alcabala'),
    path('crear_alcabala/', CrearAlcabala.as_view(), name='crear_alcabala'),
    path('get_personas/', GetPersonas.as_view(), name='get_personas'),
    path('revision_alcabala/', RevisionAlcabala.as_view(), name='revision_alcabala'),
    path('report_alcabala/<int:pk>/', ReportAlcabala.as_view(), name='report_alcabala'),
]
