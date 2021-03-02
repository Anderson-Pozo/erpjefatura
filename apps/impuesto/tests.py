from django.test import TestCase
from apps.impuesto.models import Impuesto, calcular_impuesto


# Create your tests here.
class ImpuestoTest(TestCase):
    def setUp(self) -> None:
        Impuesto.objects.create(
            numero=0,
            fraccion_basica=0,
            fraccion_excedente=600,
            impuesto_fraccion_basica=10,
            porcentaje_fraccion_excedente=0.00
        )

    def test_calc_impuesto(self):
        row = Impuesto.objects.get(fraccion_basica__lt=500, fraccion_excedente__gte=500)
        diferencia = 500 - row.fraccion_basica
        suma = row.impuesto_fraccion_basica + (diferencia * row.porcentaje_fraccion_excedente)
        self.assertEqual(suma, 10.00)
