from datetime import date
from django.test import TestCase
from apps.alcabala.models import Alcabala, Persona, Predio
from apps.direccion.models import Direccion, Barrio, Parroquia
from apps.plusvalia.models import Plusvalia


class PlusvaliaTest(TestCase):
    def setUp(self) -> None:
        parroquia_test = Parroquia.objects.create(
            nombre='Mariscal'
        )
        barrio_test = Barrio.objects.create(
            nombre='Sur',
            zona='Urbana',
            parroquia=parroquia_test
        )
        direccion_test = Direccion.objects.create(
            calle_principal='Juan Acosta',
            calle_secundaria='8 Diciembre',
            barrio=barrio_test
        )
        predio_test = Predio.objects.create(
            clave_catastral='1111102102151212555',
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
        alcabala_test = Alcabala.objects.create(
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
        Plusvalia.objects.create(
            id=1,
            fecha_tramite=date(2010, 5, 25),
            fecha_escritura=date(2020, 6, 15),
            precio_venta=18563.8,
            precio_adquisicion=20000.59,
            rebaja_desvalorizacion=5000.00,
            rebaja_mejoras=15.56,
            utilidad_imponible=5.00,
            alcabala=alcabala_test
        )

    def test_get_total_plusvalia(self):
        plusvalia = Plusvalia.objects.get(id=1)
        self.assertEqual(plusvalia.get_total(), format(270.56, '.2f'))

    def test_get_dict_model(self):
        plusvalia = Plusvalia.objects.get(id=1)
        self.assertEqual(type(plusvalia.to_json()), type({}))
