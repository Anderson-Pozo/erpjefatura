from django import forms
from .models import Multa


class MultaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['multa'].queryset = Multa.objects.all()

    class Meta:
        model = Multa
        fields = '__all__'
        # exclude = ''
        error_messages = {
            'anio': {
                'required': 'El año es obligatorio'
            },
            'mes': {
                'required': 'El mes es obligatorio'
            },
            'porcentaje': {
                'required': 'El porcentaje es obligatorio'
            },

        }
        labels = {
            'anio': 'Año',
            'mes': 'Mes',
            'porcentaje': 'Porcentaje'

        }
        widgets = {
            'anio': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el año',
                    'required': True,
                }
            ),
            'mes': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': True,
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
