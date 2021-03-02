from datetime import date, datetime
from django.db import models
from django.forms import model_to_dict
from django.utils.timezone import now
from apps.contribuyente.models import Contribuyente
from apps.establecimiento.models import Establecimiento
from apps.impuesto.models import Impuesto, calcular_impuesto, calc_meses_multa
from apps.auditoria.mixins import AuditMixin

from apps.utils.calc_months import calcular_meses


# Create your models here.
class Patente(AuditMixin, models.Model):
    """
    Modelo de Pantente que contiene los datos de la patente
    municipal y su relación con el establecimiento
    """
    id = models.AutoField(primary_key=True)
    numero_patente = models.IntegerField('Número de patente', blank=True, null=True)
    fecha = models.DateField('Fecha', blank=True, null=True)
    exonerada = models.BooleanField('Patente exonerada', blank=True, null=True, default=False)
    suspendida = models.BooleanField('Patente suspendida', blank=True, null=True, default=False)
    contribuyente = models.ForeignKey(Contribuyente, on_delete=models.CASCADE)
    establecimiento = models.ForeignKey(Establecimiento, on_delete=models.CASCADE)

    def __str__(self):
        return 'Patente Nº {}'.format(self.id)

    def get_estado(self):
        # if (self.suspendida and self.exonerada) is False:
        #     return '<span class="badge badge-light">Normal</span>'
        if self.suspendida:
            return '<span class="badge badge-danger">Suspendida</span>'
        elif self.exonerada:
            return '<span class="badge badge-success">Exonerada</span>'
        else:
            return '<span class="badge badge-light">Sin estado</span>'

    def to_json(self):
        item = model_to_dict(self)
        item['ruc'] = self.contribuyente.ruc
        item['tipocontribuyente'] = self.contribuyente.tipocontribuyente.nombre
        item['nombre_establecimiento'] = self.establecimiento.nombre
        item['total_patrimonio'] = self.establecimiento.total_patrimonio
        item['nombre_contribuyente'] = self.contribuyente.get_nombre(self.contribuyente.ruc)
        item['estado'] = self.get_estado()
        return item

    def get_impuesto(self):
        return calcular_impuesto(self.establecimiento.total_patrimonio)

    def get_ultimo_pago(self):
        return fecha_ultimo_pago(self.id)

    def get_vencimiento(self):
        ultimo_anio = self.get_ultimo_pago().year
        anio_actual = datetime.now().year

        if ultimo_anio == anio_actual:
            fecha_vencimiento = self.contribuyente.get_fecha_vencimiento().replace(year=anio_actual)
            return fecha_vencimiento
        else:
            fecha_vencimiento = self.contribuyente.get_fecha_vencimiento().replace(year=ultimo_anio+1)
            return fecha_vencimiento

    def get_interes(self):
        fecha_actual = date.today()
        fecha_vencimiento = self.get_vencimiento()

        if fecha_actual > fecha_vencimiento:
            meses_retraso = calcular_meses(fecha_vencimiento, fecha_actual)
            impuesto = float(self.get_impuesto())
            total = impuesto * meses_retraso * 0.03
            return format(total, '.2f')
        else:
            return format(0.00, '.2f')

    def get_multa(self):
        fecha_vencimiento = self.get_vencimiento()
        fecha_actual = date.today()
        impuesto = float(self.get_impuesto())

        if fecha_actual > fecha_vencimiento:
            suma = 0.0
            multas = calc_meses_multa(fecha_vencimiento, fecha_actual)
            for i in multas:
                suma += impuesto * float(i.porcentaje)
            return format(suma, '.2f')
        else:
            return format(0.00, '.2f')

    class Meta:
        db_table = "patente"


class DetallePatente(AuditMixin, models.Model):
    """
    El modelo DetallePatente almacena un historico de los
    movimientos de patente, ya se apertura o renovación
    """
    id = models.AutoField(primary_key=True)
    fecha = models.DateField('Fecha de tramite', default=now, blank=True, null=True)
    impuesto = models.DecimalField(
        'Impuesto',
        decimal_places=2,
        default=0.00,
        max_digits=9,
        blank=True,
        null=True
    )
    interes = models.DecimalField(
        'Interes',
        decimal_places=2,
        default=0.00,
        max_digits=9,
        blank=True,
        null=True
    )
    multa = models.DecimalField(
        'Multa',
        decimal_places=2,
        default=0.00,
        max_digits=9,
        blank=True,
        null=True
    )
    servicios_administrativos = models.DecimalField(
        'Servicios administrativos',
        decimal_places=2,
        default=0.99,
        max_digits=9,
        blank=True,
        null=True
    )
    patente = models.ForeignKey(Patente, on_delete=models.CASCADE)

    def __str__(self):
        return 'Detalle patente {}'.format(self.id)

    def get_total(self):
        total = self.impuesto + self.interes + self.multa + self.servicios_administrativos
        return format(total, '.2f')

    def to_json(self):
        item = model_to_dict(self)
        return item

    class Meta:
        db_table = "detalle_patente"


def fecha_ultimo_pago(id_patente):
    try:
        fecha = DetallePatente.objects.filter(patente__id=id_patente).order_by('-fecha')[0]
        return fecha.fecha
    except IndexError:
        return date.today()
