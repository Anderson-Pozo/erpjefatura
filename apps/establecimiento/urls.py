from django.urls import path
from .views import IndexEstablecimiento

urlpatterns = [
    path('', IndexEstablecimiento.as_view(), name='lista_establecimientos'),
]

# URL Implicit views
urlpatterns += [
    # path('index_contribuyente/', login_required(TemplateView.as_view(
    #         template_name='user/list_users.html'
    # ), name='home_users'),
]
