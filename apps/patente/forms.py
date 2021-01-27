from django import forms
from .models import Patente, DetallePatente
from apps.contribuyente.models import Contribuyente
from apps.establecimiento.models import Establecimiento


class PatenteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['multa'].queryset = Multa.objects.all()

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
                    'type': 'date',
                }
            ),
            'contribuyente': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'value': Contribuyente.objects.last().ruc,
                    'readonly': True
                }
            ),
            'establecimiento': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'value': Establecimiento.objects.last().nombre,
                    'readonly': True
                }
            ),

        }
