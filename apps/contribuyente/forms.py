from django import forms
from .models import Contribuyente, TipoContribuyente


class ContribuyenteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tipocontribuyente'].queryset = TipoContribuyente.objects.all()

    class Meta:
        model = Contribuyente
        fields = (
            'ruc',
            'numero_cedula',
            'nombres',
            'apellidos',
            'nacionalidad',
            'email',
            'tlf_celular',
            'tlf_convencional',
            'tipocontribuyente'
        )
        labels = {
            'ruc': 'RUC',
            'numero_cedula': 'Número de cédula',
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'nacionalidad': 'Nacionalidad',
            'email': 'Correo electrónico',
            'tlf_celular': 'Teléfono celular',
            'tlf_convencional': 'Teléfono convencional',
            'tipocontribuyente': 'Tipo de persona'
        }
        widgets = {
            'ruc': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el RUC',
                    'required': True,
                }
            ),
            'numero_cedula': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el número de cédula',
                    'required': True,
                }
            ),
            'nombres': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese los nombres',
                    'required': True,
                }
            ),
            'apellidos': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese los apellidos',
                    'required': True,
                }
            ),
            'nacionalidad': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la nacionalidad',
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el correo electrónico',
                }
            ),
            'tlf_celular': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el teléfono celular',
                }
            ),
            'tlf_convencional': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el teléfono convencional',
                }
            ),
            'tipocontribuyente': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            )
        }
