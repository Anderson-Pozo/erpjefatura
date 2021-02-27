from django import forms
from datetime import datetime, date
from .models import Plusvalia


class PlusvaliaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Plusvalia
        fields = '__all__'
        # exclude = ''
        error_messages = {
            # 'vendedor': {
            #     'required': 'El vendedor es obligatorio'
            # },
            # 'comprador': {
            #     'required': 'El comprador es obligatorio'
            # },
            'valor_escritura': {
                'required': 'El valor de la escritura es obligatorio'
            },
            'valor_notaria': {
                'required': 'El valor de la notaria es obligatorio'
            },
            'precio_venta': {
                'required': 'El precio de venta es obligatorio'
            },
            'precio_adquisicion': {
                'required': 'El precio de adquisicion es obligatorio'
            },
            'rebaja_mejoras': {
                'required': 'El impuesto de rebaja por mejoras es obligatorio'
            },
            'diferenicia_neta': {
                'required': 'La diferencia neta es obligatoria'
            },
            'tenencia': {
                'required': 'La tenencia es obligatoria'
            },
            'base_rebajar_moneda': {
                'required': 'La base para rebajar por Desvalorización Moneda es obligatoria'
            },
            'rebaja_desvalorizacion': {
                'required': 'La rebaja por Desvalorización Moneda es obligatoria'
            },
            'utilidad_imponible': {
                'required': 'La utilidad imponible es obligatoria'
            },
        }

        widgets = {
            'numero': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el numero',
                    'required': True,
                }
            ),
            'fecha_escritura': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'value': date.today(),
                    'type': 'date',
                }
            ),
            'fecha_tramite': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'value': date.today(),
                    'type': 'date',
                }
            ),
            # 'valor_escritura': forms.NumberInput(
            #     attrs={
            #         'class': 'form-control',
            #         'placeholder': 'Ingrese el valor inicial',
            #         'required': True,
            #     }
            # ),
            # 'valor_notaria': forms.NumberInput(
            #     attrs={
            #         'class': 'form-control',
            #         'placeholder': 'Ingrese el valor actual',
            #         'required': True,
            #     }
            # ),
            'precio_venta': forms.NumberInput(
                attrs={
                    'class': 'form-control form-control-sm',
                    'required': True,
                }
            ),
            'precio_adquisicion': forms.NumberInput(
                attrs={
                    'class': 'form-control form-control-sm',
                    'required': True,
                }
            ),
            'diferencia_bruta': forms.NumberInput(
                attrs={
                    'class': 'form-control form-control-sm',
                    'required': True,
                }
            ),
            'rebaja_mejoras': forms.NumberInput(
                attrs={
                    'class': 'form-control form-control-sm',
                    'required': True,
                }
            ),
            'diferencia_neta': forms.NumberInput(
                attrs={
                    'class': 'form-control form-control-sm',
                    'required': True,
                }
            ),
            'tenencia': forms.NumberInput(
                attrs={
                    'class': 'form-control form-control-sm',
                    'required': True,
                    'type': 'number'
                }
            ),
            'base_rebajar_moneda': forms.NumberInput(
                attrs={
                    'class': 'form-control form-control-sm',
                    'required': True,
                    'type': 'number'
                }
            ),
            'rebaja_desvalorizacion': forms.NumberInput(
                attrs={
                    'class': 'form-control form-control-sm',
                    'required': True,
                    'type': 'number'
                }
            ),
            'utilidad_imponible': forms.NumberInput(
                attrs={
                    'class': 'form-control form-control-sm',
                    'required': True,
                }
            ),

        }
