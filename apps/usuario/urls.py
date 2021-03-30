from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('account/', Account.as_view(), name='account'),
    path('change_password/', ChangePassword.as_view(), name='change_password'),
]

# URL Admin actions
urlpatterns += [
    path('lista_usuarios/', ListaUsuarios.as_view(), name='lista_usuarios'),
    path('crear_usuario/', CrearUsuario.as_view(), name='crear_usuario'),
    path('editar/<int:pk>/', EditarUsuario.as_view(), name='editar_usuario'),
    path('eliminar/<int:pk>/', EliminarUsuario.as_view(), name='eliminar_usuario'),
]

# URL Logs
urlpatterns += [
    path('lista_logs/', ListaLogs.as_view(), name='lista_logs'),
]

# URL Grupos
urlpatterns += [
    path('lista_grupo/', ListaGrupo.as_view(), name='lista_grupo'),
    path('crear_grupo/', CrearGrupo.as_view(), name='crear_grupo'),
    path('editar_grupo/<int:pk>/', EditarGrupo.as_view(), name='editar_grupo'),
]

# URL Permisos
urlpatterns += [
    path('lista_permisos/', ListaPermisos.as_view(), name='lista_permisos'),
]
