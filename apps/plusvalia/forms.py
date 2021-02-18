from django import forms
from .models import Plusvalia,Alcabala
from apps.alcabala.models import Vendedor,Comprador


class PlusvaliaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['alcabala'].queryset = Alcabala.objects.all()
        # self.fields['vendedor'].queryset = Vendedor.objects.all()
        # self.fields['comprador'].queryset = Comprador.objects.all()



    class Meta:
        model = Plusvalia
        fields = '__all__'
        # exclude = ''
        error_messages = {
            'vendedor': {
                'required': 'El vendedor es obligatorio'
            },
            'comprador': {
                'required': 'El comprador es obligatorio'
            },
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
            'valor_escritura': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el valor USD',
                    'required': True,
                }
            ),
            'valor_notaria': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el avaluo comercial',
                    'required': True,
                }
            ),
            'precio_venta': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el precio de venta',
                    'required': True,
                }
            ),
            'precio_adquisicion': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el precio de adquisición',
                    'required': True,
                }
            ),
            'diferencia_bruta': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la diferencia bruta',
                    'required': True,
                }
            ),
            'rebaja_mejoras': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el valor de mejoras',
                    'required': True,
                }
            ),
            'diferencia_neta': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la diferencia neta',
                    'required': True,
                }
            ),
            'tenencia': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el 5% c/año de tenencia',
                    'required': True,
                }
            ),
            'base_rebajar_moneda': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la base para rebajar por Desvalorización Moneda',
                    'required': True,
                }
            ),
            'rebaja_desvalorizacion': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la rebaja por Desvalorización Moneda',
                    'required': True,
                }
            ),
            'utilidad_imponible': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la Utilidad Imponible',
                    'required': True,
                }
            ),

        }