from django.db import models
from django.forms import model_to_dict
from apps.alcabala.models import Alcabala
from apps.auditoria.mixins import AuditMixin


# Create your models here.
class Plusvalia(AuditMixin, models.Model):
    """
    Clase Plusvalia que contiene los campos de la entidad
    plusvalia y su relacion con la entidad Alcabala
    """
    id = models.AutoField(primary_key=True)
    numero = models.IntegerField('Número de plusvalia', blank=True, null=True)
    fecha_tramite = models.DateField('Fecha del tramite', blank=True, null=True)
    fecha_escritura = models.DateField('Fecha de la escritura', blank=True, null=True)
    # fecha_notaria = models.DateField('Fecha de la notaria', blank=True, null=True)
    valor_escritura = models.DecimalField(
        'Valor del predio',
        decimal_places=2,
        default=0.00,
        max_digits=9,
        blank=False,
        null=True
    )
    valor_notaria = models.DecimalField(
        'Valor de cuantia de la notaria',
        decimal_places=2,
        default=0.00,
        max_digits=9,
        blank=False,
        null=True
    )
    precio_venta = models.DecimalField(
        'Precio de venta',
        decimal_places=2,
        default=0.00,
        max_digits=9,
        blank=False,
        null=True
    )
    precio_adquisicion = models.DecimalField(
        'Precio de adquisición',
        decimal_places=2,
        default=0.00,
        max_digits=9,
        blank=False,
        null=True
    )
    diferencia_bruta = models.DecimalField(
        'Diferencia bruta',
        decimal_places=2,
        default=0.00,
        max_digits=9,
        blank=False,
        null=True
    )
    rebaja_mejoras = models.DecimalField(
        'Rebaja por mejoras',
        decimal_places=2,
        default=0.00,
        max_digits=9,
        blank=False,
        null=True
    )
    diferencia_neta = models.DecimalField(
        'Diferencia neta',
        decimal_places=2,
        default=0.00,
        max_digits=9,
        blank=False,
        null=True
    )
    tenencia = models.DecimalField(
        'Tenencia',
        decimal_places=2,
        default=0.00,
        max_digits=9,
        blank=False,
        null=True
    )
    base_rebajar_moneda = models.DecimalField(
        'Base para rebajar moneda',
        decimal_places=2,
        default=0.00,
        max_digits=9,
        blank=False,
        null=True
    )
    rebaja_desvalorizacion = models.DecimalField(
        'Rebaja por desvalorización',
        decimal_places=2,
        default=0.00,
        max_digits=9,
        blank=False,
        null=True
    )
    utilidad_imponible = models.DecimalField(
        'Utilidad imponible',
        decimal_places=2,
        default=0.00,
        max_digits=9,
        blank=False,
        null=True
    )
    alcabala = models.ForeignKey(Alcabala, on_delete=models.CASCADE)
    def to_json(self):
        item = model_to_dict(self)
        item['comprador'] = '{} {}'.format(self.alcabala.comprador.nombres, self.alcabala.comprador.apellidos)
        item['vendedor'] = '{} {}'.format(self.alcabala.vendedor.nombres, self.alcabala.vendedor.apellidos)
        return item

    class Meta:
        db_table = "plusvalia"
