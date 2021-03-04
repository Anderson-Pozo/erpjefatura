import decimal
from datetime import date
from django.test import TestCase
from apps.impuesto.models import Impuesto, calcular_impuesto


# Create your tests here.
class ImpuestoTest(TestCase):
    impuestos = [
        [1, 0, 600, 10, 0.0],
        [2, 600, 800, 10, 0.03500],
        [3, 800, 1000, 17, 0.01502],
        [4, 1000, 1200, 20, 0.01000],
        [5, 1200, 1500, 22, 0.02000],
        [6, 1500, 3000, 28, 0.00933],
        [7, 3000, 4000, 42, 0.01400],
        [8, 4000, 5000, 56, 0.02800],
        [9, 5000, 10000, 84, 0.00280],
        [10, 10000, 20000, 98, 0.00140],
        [11, 20000, 30000, 112, 0.00280],
        [12, 30000, 50000, 140, 0.00700],
        [13, 50000, 70000, 280, 0.00700],
        [14, 70000, 90000, 420, 0.00700],
        [15, 90000, 120000, 560, 0.70000],
        [16, 120000, 150000, 770, 0.00500],
        [17, 150000, 200000, 920, 0.00600],
        [18, 200000, 300000, 1220, 0.00400],
        [19, 300000, 500000, 1620, 0.00400],
        [20, 500000, 1000000, 2420, 0.00117],
        [21, 1000000, 9999999, 3005, 0.0],
    ]
    capital = decimal.Decimal(550.00)

    def setUp(self) -> None:
        for i in self.impuestos:
            Impuesto.objects.create(
                numero=i[0],
                fraccion_basica=i[1],
                fraccion_excedente=i[2],
                impuesto_fraccion_basica=i[3],
                porcentaje_fraccion_excedente=i[4]
            )

    def test_calc_impuesto(self):
        row = Impuesto.objects.get(fraccion_basica__lt=self.capital, fraccion_excedente__gte=self.capital)
        diferencia = self.capital - row.fraccion_basica
        suma = decimal.Decimal(row.impuesto_fraccion_basica) + (diferencia * row.porcentaje_fraccion_excedente)
        res = decimal.Decimal(suma,)
        self.assertEqual(res, 10.00)

    def test_get_fraccion(self):
        row = Impuesto.objects.get(fraccion_basica__lt=self.capital, fraccion_excedente__gte=self.capital)
        fraccion = row.fraccion_basica
        self.assertEqual(fraccion, 0)
