from datetime import date
from django.test import TestCase
from apps.patente.models import Patente, DetallePatente
from apps.establecimiento.models import Establecimiento, TipoActividad
from apps.contribuyente.models import Contribuyente, TipoContribuyente, Natural, Juridico
from apps.direccion.models import Direccion, Barrio, Parroquia


class ContribuyenteTest(TestCase):
    def setUp(self) -> None:
        tp_contribuyente_test = TipoContribuyente.objects.create(
            nombre='Natural',
            obligado_contabilidad=False
        )
        tp_contribuyente_juridico = TipoContribuyente.objects.create(
            nombre='Juridico',
            obligado_contabilidad=True
        )
        Natural.objects.create(
            ruc='0401798475001',
            email='anderam92@gmail.com',
            tlf_celular='0965250869',
            tlf_convencional='2973486',
            nombres='Anderson Manuel',
            apellidos='Prado Fuertes',
            estado=True,
            tipocontribuyente=tp_contribuyente_test
        )
        Juridico.objects.create(
            ruc='0401798475777',
            email='andrram92@gmail.com',
            tlf_celular='0965250869',
            tlf_convencional='2973486',
            cedula_representante='0401798477',
            razon_social='Cooperativa Huaca',
            tipocontribuyente=tp_contribuyente_juridico
        )

    def test_get_nombre_natural(self):
        contribuyente = Contribuyente.objects.get(ruc='0401798475001')
        self.assertEqual(contribuyente.get_nombre_contri(), 'Anderson Manuel Prado Fuertes')

    def test_get_nombre_juridico(self):
        contribuyente_juridico = Contribuyente.objects.get(ruc='0401798475777')
        self.assertEqual(contribuyente_juridico.get_nombre_contri(), 'Cooperativa Huaca')


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

    def test_get_dict_model(self):
        patente = Patente.objects.get(numero_patente=451289)
        self.assertEqual(type(patente.to_json()), type({}))
