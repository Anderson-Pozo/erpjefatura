from django.urls import path
from .views import Index

urlpatterns = [
    path('index_contribuyente/', Index.as_view(), name='index_contribuyente'),
    # path('help_contribuyente', Help.as_view(), name='help_contribuyente'),
]
