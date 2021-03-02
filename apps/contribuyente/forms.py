from django import forms
from .models import Natural, Juridico, TipoContribuyente


class ContribuyenteNaturalForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tipocontribuyente'].initial = TipoContribuyente.objects.get(id=1)
        # self.fields['contribuyente'].initial = Contribuyente.objects.last()

    class Meta:
        model = Natural
        fields = '__all__'
        exclude = ['estado']
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
            'nacionalidad': forms.Select(
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
                    'required': True,
                    'readonly': True
                }
            ),
            'adulto': forms.CheckboxInput(
                attrs={
                    'class': 'custom-control-input',
                    'type': 'checkbox',
                }
            ),
            'artesano': forms.CheckboxInput(
                attrs={
                    'class': 'custom-control-input',
                    'type': 'checkbox',
                }
            ),
        }


class ContribuyenteJuridicoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tipocontribuyente'].initial = TipoContribuyente.objects.get(id=2)

    class Meta:
        model = Juridico
        fields = '__all__'
        exclude = ['estado']
        error_messages = {
            'ruc': {
                'max_length': 'El ruc solo debe tener 13 dígitos',
                'required': 'El ruc es obligatorio'
            },
            'razon_social': {
                'required': 'La razón social es obligatoria'
            },
            'tipocontribuyente': {
                'required': 'El tipo de persona no puede estar vacío'
            },
            'cedula_representante': {
                'required': 'La cedula del representante es requerida'
            },
            'nombres_representante': {
                'required': 'Los nombres del representante son requeridos'
            },
            'apellidos_representante': {
                'required': 'Los apellidos del representante son requeridos'
            }
        }
        widgets = {
            'ruc': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el RUC',
                    'required': True,
                }
            ),
            'razon_social': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nombre o razón social',
                    'required': True,
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
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el correo electrónico',
                }
            ),
            'tipocontribuyente': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'readonly': True
                }
            ),
            'cedula_representante': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la cédula representante',
                    'required': True,
                }
            ),
            'nombres_representante': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese los nombres del representante',
                    'required': True,
                }
            ),
            'apellidos_representante': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese los apellidos del representante',
                    'required': True,
                }
            ),
            'telefono_representante': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el número de teléfono del representante',
                    'required': True,
                }
            ),
            'correo_representante': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el correo del representante',
                    'required': True,
                }
            ),
        }
