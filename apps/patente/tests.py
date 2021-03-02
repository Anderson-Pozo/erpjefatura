from datetime import date
from django.test import TestCase
from apps.patente.models import Patente, DetallePatente
from apps.establecimiento.models import Establecimiento, TipoActividad
from apps.contribuyente.models import Contribuyente, TipoContribuyente
from apps.direccion.models import Direccion, Barrio, Parroquia


# Create your tests here.
class PatenteTest(TestCase):
    def setUp(self) -> None:
        tp_contribuyente_test = TipoContribuyente.objects.create(
            nombre='Natural',
            obligado_contabilidad=False
        )
        tp_actividad_test = TipoActividad.objects.create(
            tipo_actividad='Economica'
        )
        parroquia_test = Parroquia.objects.create(
            nombre='Huaca'
        )
        barrio_test = Barrio.objects.create(
            nombre='Centro',
            zona='Rural',
            parroquia=parroquia_test
        )
        direccion_test = Direccion.objects.create(
            calle_principal='Juan Montalvo',
            calle_secundaria='8 Diciembre',
            barrio=barrio_test
        )
        establecimiento_test = Establecimiento.objects.create(
            nombre='Carniceria Manuel',
            descripcion_actividad='Carnes de venta',
            fecha_inicio_actividad=date.today(),
            total_patrimonio=1258.25,
            tipo_venta='Comercial',
            situacion_legal='Propio',
            estado=True,
            tipo_actividad=tp_actividad_test,
            direccion=direccion_test
        )
        contribuyente_test = Contribuyente.objects.create(
            ruc='0401798475001',
            email='anderam92@gmail.com',
            tlf_celular='0965250869',
            tlf_convencional='2973486',
            estado=True,
            tipocontribuyente=tp_contribuyente_test
        )
        Patente.objects.create(
            numero_patente=451289,
            fecha=date.today(),
            exonerada=True,
            suspendida=False,
            contribuyente=contribuyente_test,
            establecimiento=establecimiento_test
        )

    def test_patente_estado(self):
        patente = Patente.objects.get(numero_patente=451289)
        self.assertEqual(patente.get_estado(), '<span class="badge badge-success">Suspendida</span>')

    def test_patente_impuesto(self):
        patente = Patente.objects.get(numero_patente=451289)
        self.assertEqual(patente.get_impuesto(), 25.25)
