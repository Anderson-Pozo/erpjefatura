from django.contrib.auth.forms import AuthenticationForm
from django import forms
from apps.usuario.models import User, Grupo


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.fields['password'].widget.attrs['class'] = 'form-control form-control-user'
        self.fields['password'].widget.attrs['placeholder'] = 'Ingrese su contraseña'

    username = forms.CharField(
        required=True,
        max_length=13,
        label='Ingrese su número de RUC',
        help_text='Ingrese el número completo de su RUC',
        error_messages={
            'required': 'Número de RUC es requerido',
            'maxlength': 'El número de RUC debe tener 13 dígitos'
        },
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'pattern': '[0-9]+',
                'minlength': '10',
                'placeholder': 'Ingrese su número de RUC',
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
        required=False,
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
            "Ingrese un número de RUC y contraseña válidos"
        ),
    }


class UserForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese la constraseña',
                'id': 'password1',
                'required': 'required'
            }
        )
    )
    password2 = forms.CharField(
        label='Confirma la contraseña',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirme la contraseña',
                'id': 'password2',
                'required': 'required'
            }
        )
    )

    class Meta:
        model = User
        fields = {
            'email',
            'username',
            'first_name',
            'last_name',
            'is_superuser',
            'is_active',
            'is_staff',
            'groups',
            'user_permissions'
        }
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el correo electrónico'
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su número de cédula'
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese sus nombres'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese sus apellidos'
                }
            ),
            'is_superuser': forms.CheckboxInput(
                attrs={
                    'class': 'custom-control-input',
                    'type': 'checkbox',
                }
            ),
            'is_active': forms.CheckboxInput(
                attrs={
                    'class': 'custom-control-input',
                    'type': 'checkbox',
                }
            ),
            'is_staff': forms.CheckboxInput(
                attrs={
                    'class': 'custom-control-input',
                    'type': 'checkbox',
                }
            ),
            'groups': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            ),
            'user_permissions': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            )
        }

    def clean_password2(self):
        """
        Validates if the two passwords are the same
        :return: Password valid
        :exception: when two passwords are not the same
        """
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')

        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class AccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {
            'email',
            'username',
            'first_name',
            'last_name',
            'image'
            # 'path_avatar'
        }
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el correo electrónico'
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su número de cédula',
                    'readonly': True
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese sus nombres'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese sus apellidos'
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'type': 'file',
                    'accept': "image/*",
                    'hidden': True
                }
            ),
            # 'path_avatar': forms.TextInput(
            #     attrs={
            #         'class': 'form-control',
            #         'placeholder': 'Ingrese el correo electrónico',
            #     }
            # ),
        }


class RecoverPasswordForm(forms.Form):
    numero_ruc = forms.CharField(
        required=True,
        max_length=13,
        label='Ingrese su número de RUC',
        help_text='Ingrese el número completo de su RUC',
        error_messages={
            'required': 'Número de RUC es requerido',
            'maxlength': 'El número de RUC debe tener 13 dígitos'
        },
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'pattern': '[0-9]+',
                'minlength': '10',
                'placeholder': 'Ingrese su número de RUC',
            }
        )
    )


class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = {
            'name',
            'permissions',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm',
                    'placeholder': 'Ingrese el nombre del grupo'
                }
            ),
            'permissions': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            )
        }
