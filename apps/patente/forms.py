from datetime import datetime

from django import forms
from datetime import datetime
from .models import Patente, DetallePatente
from apps.contribuyente.models import Contribuyente
from apps.establecimiento.models import Establecimiento


class PatenteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['contribuyente'].initial = Contribuyente.objects.last()
        self.fields['establecimiento'].initial = Establecimiento.objects.last()

    class Meta:
        model = Patente
        fields = '__all__'
        # exclude = ''
        error_messages = {
            'fecha': {
                'required': 'La fecha es obligatoria'
            },
            'contribuyente': {
                'required': 'Seleccione el contribuyente'
            },
            'establecimiento': {
                'required': 'Seleccione el establecimiento'
            },
        }

        widgets = {
            'fecha': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'value': datetime.now().strftime('%Y-%m-%d'),
                    'type': 'date',
                }
            ),
            'numero_patente': forms.NumberInput(
                # format='%Y-%m-%d',
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'type': 'number',
                }
            ),
            'contribuyente': forms.Select(
                attrs={
                    'class': 'form-control',
                    # 'required': True,
                    'readonly': True
                }
            ),
            'establecimiento': forms.Select(
                attrs={
                    'class': 'form-control',
                    # 'required': True,
                    'readonly': True
                    # 'value': Establecimiento.objects.last().id,
                }
            ),

        }


class DetalleForm(forms.ModelForm):
    patente = Patente.objects.last()

    class Meta:
        model = DetallePatente
        fields = '__all__'
        error_messages = {
            'fecha': {
                'required': 'La fecha es obligatoria'
            },
            'impuesto': {
                'required': 'El impuesto es obligatorio'
            },
            'interes': {
                'required': 'El interes es requerido'
            },
            'multa': {
                'required': 'El valor de multa es requerido'
            },
            'servicios_administrativos': {
                'required': 'Los servicios administrativos son requeridos'
            },
        }
        widgets = {
            'fecha': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'class': 'form-control form-control-sm',
                    'required': True,
                    'value': datetime.now().strftime('%Y-%m-%d'),
                    'type': 'date',
                }
            ),
            'impuesto': forms.NumberInput(
                attrs={
                    'class': 'form-control form-control-sm',
                    'required': True,
                    'step': '0.01'
                }
            ),
            'interes': forms.NumberInput(
                attrs={
                    'class': 'form-control form-control-sm',
                    'required': True,
                    'step': '0.01'
                }
            ),
            'multa': forms.NumberInput(
                attrs={
                    'class': 'form-control form-control-sm',
                    'required': True,
                    'step': '0.01'
                }
            ),
            'servicios_administrativos': forms.NumberInput(
                attrs={
                    'class': 'form-control form-control-sm',
                    'required': True,
                    'step': '0.01'
                }
            ),

        }
