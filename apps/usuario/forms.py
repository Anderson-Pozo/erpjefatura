from django.contrib.auth.forms import AuthenticationForm
from django import forms
from apps.usuario.models import User


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.fields['password'].widget.attrs['class'] = 'form-control form-control-user'
        self.fields['password'].widget.attrs['placeholder'] = 'Ingrese su contraseña'

    username = forms.CharField(
        required=True,
        max_length=10,
        label='Ingrese su número de cédula',
        help_text='Ingrese su número de cédula de 10 dígitos',
        error_messages={
            'required': 'Número de cédula es requerido',
            'max_length': 'El número de cédual debe tener 10 dígitos'
        },
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'pattern': '[0-9]+',
                'minlength': '10',
                'placeholder': 'Ingrese su número de cédula',
            }
        )
    )

    password = forms.CharField(
        error_messages={
            'required': 'La contraseña es requerida',
        },
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'placeholder': 'Ingrese su contraseña',
            }
        )
    )

    remember_me = forms.BooleanField(
        # required=False,
        label='Guardar contraseña',
        widget=forms.CheckboxInput(
            attrs={
                'class': 'custom-control-input',
                'type': 'checkbox',
            }
        )
    )

    error_messages = {
        'invalid_login': (
            "Ingrese un número de cédula y contraseña válidos"
        ),
    }

