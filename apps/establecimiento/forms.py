from django import forms
from .models import Establecimiento, TipoActividad
from apps.direccion.models import Direccion


class EstablecimientoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tipo_actividad'].queryset = TipoActividad.objects.all()
        self.fields['direccion'].queryset = Direccion.objects.all()

    class Meta:
        model = Establecimiento
        fields = '__all__'
        # exclude = ''
        error_messages = {
            'nombre': {
                'required': 'El nombre es obligatorio'
            },
            'descripcion_actividad': {
                'required': 'La descripción es obligatoria'
            },
            'fecha_inicio_actividad': {
                'required': 'La fecha de inicio es obligatoria'
            },
            'total_patrimonio': {
                'required': 'El patrimonio es obligatorio'
            },
            'direccion': {
                'required': 'La dirección es obligatoria'
            },
            'tipo_actividad': {
                'required': 'El tipo de actividad es obligatoria'
            },
            'tipo_venta': {
                'required': 'El tipo de venta es obligatorio'
            },
            'situacion_legal': {
                'required': 'La situación legal es obligatoria'
            },
        }

        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nombre del establecimiento',
                    'required': True,
                }
            ),
            'descripcion_actividad': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la descripción',
                    'required': True,
                }
            ),
            'fecha_inicio_actividad': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'type': 'date',
                }
            ),
            'total_patrimonio': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el patrimonio',
                    'required': True,
                }
            ),
            'direccion': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'ingrese la direccion',
                    'required': True,
                }
            ),
            'tipo_actividad': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': True,
                }
            ),
            'tipo_venta': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': True,
                }
            ),
            'situacion_legal': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': True,
                }
            ),

        }
