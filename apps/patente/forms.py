from django import forms
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
                    'required': True,
                    'disabled': True
                }
            ),
            'establecimiento': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'disabled': True
                    # 'value': Establecimiento.objects.last().id,
                }
            ),

        }
