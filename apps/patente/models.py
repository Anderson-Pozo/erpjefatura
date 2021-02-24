from datetime import datetime
from django.db import models
from django.forms import model_to_dict
from apps.contribuyente.models import Contribuyente
from apps.establecimiento.models import Establecimiento
from apps.impuesto.models import Impuesto, calcular_impuesto
from apps.auditoria.mixins import AuditMixin


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

    def get_estado(self):
        pass

    def to_json(self):
        item = model_to_dict(self)
        item['ruc'] = self.contribuyente.ruc
        item['tipocontribuyente'] = self.contribuyente.tipocontribuyente.nombre
        item['nombre_establecimiento'] = self.establecimiento.nombre
        item['total_patrimonio'] = self.establecimiento.total_patrimonio
        item['nombre_contribuyente'] = self.contribuyente.get_nombre(self.contribuyente.ruc)
        return item

    def calcular_impuesto(self):
        return calcular_impuesto(self.establecimiento.total_patrimonio)

    class Meta:
        db_table = "patente"


class DetallePatente(AuditMixin, models.Model):
    """
    El modelo DetallePatente almacena un historico de los
    movimientos de patente, ya se apertura o renovación
    """
    id = models.AutoField(primary_key=True)
    fecha = models.DateField('Fecha de tramite', default=datetime.now(), blank=True, null=True)
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

    def to_json(self):
        item = model_to_dict(self)
        return item

    class Meta:
        db_table = "detalle_patente"
