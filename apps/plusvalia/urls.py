from django.urls import path
from .views import CrearPlusvalia, ListaPlusvalia, RevisionPlusvalia, ReportPlusvalia

urlpatterns = [
    path('', ListaPlusvalia.as_view(), name='lista_plusvalia'),
    path('crear_plusvalia/', CrearPlusvalia.as_view(), name='crear_plusvalia'),

    path('revision_plusvalia/', RevisionPlusvalia.as_view(), name='revision_plusvalia'),

    path('report_plusvalia/<int:pk>/', ReportPlusvalia.as_view(), name='report_plusvalia'),
]
