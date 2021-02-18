from django.db import models
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
    fecha_notaria = models.DateField('Fecha de la notaria', blank=True, null=True)
    valor_escritura = models.FloatField('Valor del predio', blank=True, null=True)
    valor_notaria = models.FloatField('Valor de cuantia de la notaria', blank=True, null=True)
    precio_venta = models.FloatField('Precio de venta', blank=True, null=True)
    precio_adquisicion = models.FloatField('Precio de adquisición', blank=True, null=True)
    diferencia_bruta = models.FloatField('Diferencia bruta', blank=True, null=True)
    rebaja_mejoras = models.FloatField('Rebaja por mejoras', blank=True, null=True)
    diferencia_neta = models.FloatField('Diferencia neta', blank=True, null=True)
    tenencia = models.FloatField('Tenencia', blank=True, null=True)
    base_rebajar_moneda = models.FloatField('Base para rebajar moneda', blank=True, null=True)
    rebaja_desvalorizacion = models.FloatField('Rebaja por desvalorización', blank=True, null=True)
    utilidad_imponible = models.FloatField('Utilidad imponible', blank=True, null=True)
    alcabala = models.ForeignKey(Alcabala, on_delete=models.CASCADE)

    class Meta:
        db_table = "plusvalia"
