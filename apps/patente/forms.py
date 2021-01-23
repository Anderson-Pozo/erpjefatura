from django import forms
from .models import Patente,DetallePatente


class PatenteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['multa'].queryset = Multa.objects.all()

    class Meta:
        model = Patente
        fields = '__all__'
        # exclude = ''
        error_messages = {
            'numero_patente': {
                'required': 'La fecha es obligatoria'
            },
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
                    'type': 'date',
                }
            ),
            'contribuyente': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': True,
                }
            ),
            'establecimiento': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': True,
                }
            ),

        }
