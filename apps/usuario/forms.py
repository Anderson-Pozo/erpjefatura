from django.contrib.auth.forms import AuthenticationForm
from django import forms
from apps.usuario.models import User


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control form-control-user'
        self.fields['username'].widget.attrs['placeholder'] = 'Ingrese su número de cédula'
        self.fields['username'].widget.attrs['autocomplete'] = 'off'

        self.fields['password'].widget.attrs['class'] = 'form-control form-control-user'
        self.fields['password'].widget.attrs['placeholder'] = 'Ingrese su contraseña'
