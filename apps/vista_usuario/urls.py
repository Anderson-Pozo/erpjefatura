from django.urls import path
from .views import Index

urlpatterns = [
    path('index_contribuyente/', Index.as_view(), name='index_contribuyente'),
]
