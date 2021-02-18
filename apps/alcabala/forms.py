from django import forms
from .models import Alcabala,Comprador,Vendedor,Predio
from apps.direccion.models import Direccion


class AlcabalaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comprador'].queryset = Comprador.objects.all()
        self.fields['vendedor'].queryset = Vendedor.objects.all()
        self.fields['predio'].queryset = Predio.objects.all()


    class Meta:
        model = Alcabala
        fields = '__all__'
        # exclude = ''
        error_messages = {
            'vendedor': {
                'required': 'El vendedor es obligatorio'
            },
            'comprador': {
                'required': 'El comprador es obligatorio'
            },
            'descripcion_tramite': {
                'required': 'La descripción del tramite es obligatoria'
            },
            'valor_compra_venta': {
                'required': 'El valor de la compra-venta es obligatoria'
            },
            'impuesto_alcabalas': {
                'required': 'El valor de la alcabalas es obligatorio'
            },
            'alcabalas_provinciales': {
                'required': 'El valor de las alcabalas provinciales es obligatorio'
            },
            'fondos_escolares': {
                'required': 'El valor de los fonos escolares es obligatorio'
            },
            'fondos_prevencion_riesgos': {
                'required': 'El valor de los fondos de prevención de riesgos es obligatorio'
            },
            'agua_potable': {
                'required': 'El del agua potable es obligatorio'
            },
        }

        widgets = {
            'vendedor': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el vendedor',
                    'required': True,
                }
            ),
            'comprador': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el comprador',
                    'required': True,
                }
            ),
            'descripcion_tramite': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la descripción de tramite',
                    'required': True,
                }
            ),
            'valor_compra_venta': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el valor de compra-venta',
                    'required': True,
                }
            ),
            'impuesto_alcabalas': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el impuesto de alcabalas',
                    'required': True,
                }
            ),
            'alcabalas_provinciales': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el valor de las alcabalas provinciales',
                    'required': True,
                }
            ),
            'fondos_escolares': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el valor de los fondos escolares',
                    'required': True,
                }
            ),
            'fondos_prevencion_riesgos': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el valor de los fondos de prevención de riesgos',
                    'required': True,
                }
            ),
            'agua_potable': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el valor del agua potable',
                    'required': True,
                }
            ),

        }
