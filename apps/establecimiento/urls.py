from django.urls import path
from .views import ListaEstablecimiento, CrearEstablecimiento

urlpatterns = [
    path('', ListaEstablecimiento.as_view(), name='lista_establecimientos'),
    path('crear_establecimineto/', CrearEstablecimiento.as_view(), name='crear_establecimiento')
]

# URL Implicit views
urlpatterns += [
    # path('index_contribuyente/', login_required(TemplateView.as_view(
    #         template_name='user/list_users.html'
    # ), name='home_users'),
]
