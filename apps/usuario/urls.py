from django.urls import path, re_path
from .views import Account, ChangePassword

urlpatterns = [
    path('account/', Account.as_view(), name='account'),
    path('change_password/', ChangePassword.as_view(), name='change_password')
]
