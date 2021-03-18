from datetime import date
from django.test import TestCase
from apps.patente.models import Patente, DetallePatente
from apps.establecimiento.models import Establecimiento, TipoActividad
from apps.contribuyente.models import Contribuyente, TipoContribuyente
from apps.direccion.models import Direccion, Barrio, Parroquia


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
            fecha_inicio_actividad=date(2020, 12, 5),
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
        patente_test = Patente.objects.create(
            id=1,
            numero_patente=451289,
            fecha=date.today(),
            exonerada=True,
            suspendida=True,
            contribuyente=contribuyente_test,
            establecimiento=establecimiento_test
        )
        DetallePatente.objects.create(
            fecha=date.today(),
            impuesto=25.00,
            interes=0.00,
            multa=0.00,
            servicios_administrativos=0.99,
            patente=patente_test
        )

    def test_patente_estado(self):
        patente = Patente.objects.get(numero_patente=451289)
        self.assertEqual(patente.get_estado(), '<span class="badge badge-danger">Suspendida</span>')

    def test_get_ultimo_pago(self):
        query = DetallePatente.objects.filter(patente__id=1).count()
        if query == 0:
            fecha = Patente.objects.get(id=1).establecimiento.fecha_inicio_actividad
            self.assertEqual(fecha, date(2020, 12, 5))
        else:
            row = DetallePatente.objects.filter(patente__id=1).order_by('-fecha')[0]
            self.assertEqual(row.fecha, date.today())
