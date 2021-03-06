"""erpjefatura URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from erpjefatura.settings import base

from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from apps.usuario.views import Login, logout_user, RecoveryPassword
from apps.administrador.views import Index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', Login.as_view(), name='login'),
    path('logout/', login_required(logout_user), name='logout'),
    path('recover_password/', RecoveryPassword.as_view(), name='recover_password'),
    path('', Index.as_view(), name='index'),
]

# URL Apps
urlpatterns += [
    path('impuesto/', include(('apps.impuesto.urls', 'impuesto'))),
    path('usuario/', include(('apps.usuario.urls', 'usuario'))),
    path('contribuyente/', include(('apps.contribuyente.urls', 'contribuyente'))),
    path('establecimiento/', include(('apps.establecimiento.urls', 'establecimiento'))),
    path('patente/', include(('apps.patente.urls', 'patente'))),
    path('alcabala/', include(('apps.alcabala.urls', 'alcabala'))),
    path('plusvalia/', include(('apps.plusvalia.urls', 'plusvalia'))),
    path('direccion/', include(('apps.direccion.urls', 'direccion'))),
    path('consulta/', include(('apps.vista_usuario.urls', 'consulta'))),
] + static(base.MEDIA_URL, document_root=base.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
