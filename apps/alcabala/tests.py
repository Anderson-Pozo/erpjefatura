from datetime import date
from django.test import TestCase
from apps.alcabala.models import Alcabala, Persona, Predio
from apps.direccion.models import Direccion, Barrio, Parroquia


class AlcabalaTest(TestCase):
    def setUp(self) -> None:
        parroquia_test = Parroquia.objects.create(
            nombre='Huaca'
        )
        barrio_test = Barrio.objects.create(
            nombre='Centro',
            zona='Urbana',
            parroquia=parroquia_test
        )
        direccion_test = Direccion.objects.create(
            calle_principal='Juan Montalvo',
            calle_secundaria='8 Diciembre',
            barrio=barrio_test
        )
        predio_test = Predio.objects.create(
            clave_catastral='1111102102151212121',
            avaluo_comercial=52563.55,
            area_terreno=250.53,
            direccion=direccion_test
        )
        comprador_test = Persona.objects.create(
            numero_cedula='0401798475',
            nombres='Anderson Ramiro',
            apellidos='Pozo Imbaquingo',
            casado=False
        )
        vendedor_test = Persona.objects.create(
            numero_cedula='0401798111',
            nombres='Manuel Jose',
            apellidos='Rivera Cevallos',
            casado=False
        )
        Alcabala.objects.create(
            id=1,
            fecha=date(2020, 11, 15),
            descripcion_tramite='Compra venta',
            valor_compra_venta=15256.52,
            impuesto_alcabalas=25.6,
            alcabalas_provinciales=50.0,
            fondos_escolares=0.0,
            fondos_prevencion_riesgos=5.0,
            agua_potable=0.0,
            comprador=comprador_test,
            vendedor=vendedor_test,
            predio=predio_test
        )

    def test_get_zona_alcabala(self):
        alcabala = Alcabala.objects.get(id=1)
        self.assertEqual(alcabala.get_zona(), 'Urbana')

    def test_get_total_alcabala(self):
        alcabala = Alcabala.objects.get(id=1)
        self.assertEqual(alcabala.get_total(), format(80.6, '.2f'))

    def test_get_valor_compra_alcabala(self):
        alcabala = Alcabala.objects.get(id=1)
        self.assertEqual(format(alcabala.valor_compra_venta, '.2f'), format(15256.52, '.2f'))
