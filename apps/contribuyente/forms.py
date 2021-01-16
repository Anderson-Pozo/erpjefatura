from django import forms
from .models import Natural, TipoContribuyente


class ContribuyenteNaturalForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tipocontribuyente'].queryset = TipoContribuyente.objects.all()

    class Meta:
        model = Natural
        fields = '__all__'
        # exclude = ''
        error_messages = {
            'numero_cedula': {
                'max_length': 'El número de cédula solo debe tener 10 dígitos',
                'required': 'El número de cédula es obligatorio'
            },
            'ruc': {
                'max_length': 'El ruc solo debe tener 13 dígitos',
                'required': 'El ruc es obligatorio'
            },
            'nombres': {
                'required': 'Los nombres son obligatorios'
            },
            'apellidos': {
                'required': 'Los apellidos son obligatorios'
            },
            'tipocontribuyente': {
                'required': 'El tipo de persona no puede estar vacío'
            }
        }
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
