from django.urls import path, re_path
from .views import Account, ChangePassword, ListaUsuarios

urlpatterns = [
    path('account/', Account.as_view(), name='account'),
    path('change_password/', ChangePassword.as_view(), name='change_password'),
    path('lista_usuarios/', ListaUsuarios.as_view(), name='lista_usuarios')
]
