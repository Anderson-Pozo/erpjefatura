from django import forms
from datetime import datetime
from .models import Multa, Impuesto, Vencimiento


class MultaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['multa'].queryset = Multa.objects.all()

    class Meta:
        model = Multa
        fields = '__all__'
        # exclude = ''
        error_messages = {
            'fecha': {
                'required': 'La fecha es obligatoria'
            },
            'porcentaje': {
                'required': 'El porcentaje es obligatorio'
            },

        }
        labels = {
            'fecha': 'fecha',
            'porcentaje': 'Porcentaje'

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
            'porcentaje': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el porcentaje',
                    'required': True,
                }
            ),

        }


class ImpuestoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['multa'].queryset = Multa.objects.all()

    class Meta:
        model = Impuesto
        fields = '__all__'
        # exclude = ''
        error_messages = {
            'numero': {
                'required': 'El id es obligatorio'
            },
            'fraccion_basica': {
                'required': 'La fracción basica es obligatoria'
            },
            'fraccion_excedente': {
                'required': 'La fracción excedente es obligatoria'
            },
            'impuesto_fraccion_basica': {
                'required': 'El impuesto basico es obligatorio'
            },
            'porcentaje_fraccion_excedente': {
                'required': 'El porcentaje excedente es obligatorio'
            },

        }
        # labels = {
        #     'fecha': 'fecha',
        #     'porcentaje': 'Porcentaje'
        #
        # }
        widgets = {
            'numero': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el id',
                    'required': True,
                }
            ),
            'fraccion_basica': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la fracción basica',
                    'required': True,
                }
            ),
            'fraccion_excedente': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la fraccion excedente',
                    'required': True,
                }
            ),
            'impuesto_fraccion_basica': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el impuesto basico',
                    'required': True,
                }
            ),
            'porcentaje_fraccion_excedente': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el porcentaje excednete',
                    'required': True,
                }
            ),

        }


class VencimientoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['multa'].queryset = Multa.objects.all()

    class Meta:
        model = Vencimiento
        fields = '__all__'
        # exclude = ''
        error_messages = {
            'digito': {
                'required': 'el digito es obligatorio'
            },
            'no_obligado': {
                'required': 'La fecha es obligatoria'
            },
            'obligado': {
                'required': 'La fecha es obligatoria'
            },

        }
        # labels = {
        #     'fecha': 'fecha',
        #     'porcentaje': 'Porcentaje'
        #
        # }
        widgets = {
            'digito': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el digito',
                    'required': True,
                }
            ),
            'no_obligado': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'type': 'date',
                }
            ),
            'obligado': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'type': 'date',
                }
            ),

        }