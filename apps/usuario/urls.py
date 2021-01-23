from django.urls import path, re_path
from .views import Account, ChangePassword, ListaUsuarios, CrearUsuario

urlpatterns = [
    path('account/<int:pk>/', Account.as_view(), name='account'),
    path('change_password/', ChangePassword.as_view(), name='change_password'),
    path('lista_usuarios/', ListaUsuarios.as_view(), name='lista_usuarios'),
    path('crear_usuario/', CrearUsuario.as_view(), name='crear_usuario')
]
