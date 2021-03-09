from django.urls import path
from .views import send_mail_contri

urlpatterns = [
    path('mail', send_mail_contri, name='mail'),
]
