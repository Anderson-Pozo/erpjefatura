from django.db import models
from django.forms import model_to_dict
from apps.contribuyente.models import Contribuyente
from apps.establecimiento.models import Establecimiento


# Create your models here.
class Patente(models.Model):
    """
    Modelo de Pantente que contiene los datos de la patente
    municipal y su relación con el establecimiento
    """
    id = models.AutoField(primary_key=True)
    numero_patente = models.IntegerField('Número de patente', blank=True, null=True)
    exonerada = models.BooleanField('Patente exonerada', blank=True, null=True, default=False)
    suspendida = models.BooleanField('Patente suspendida', blank=True, null=True, default=False)
    contribuyente = models.ForeignKey(Contribuyente, on_delete=models.CASCADE)
    establecimiento = models.ForeignKey(Establecimiento, on_delete=models.CASCADE)

    def to_json(self):
        item = model_to_dict(self)
        item['ruc'] = self.contribuyente.ruc
        item['tipocontribuyente'] = self.contribuyente.tipocontribuyente.nombre
        item['nombre_establecimiento'] = self.establecimiento.nombre
        item['total_patrimonio'] = self.establecimiento.total_patrimonio
        return item

    class Meta:
        db_table = "patente"


class DetallePatente(models.Model):
    """
    El modelo DetallePatente almacena un historico de los
    movimientos de patente, ya se apertura o renovación
    """
    id = models.AutoField(primary_key=True)
    zona = models.CharField('Zona urbana o rural', max_length=10, blank=True, null=True)
    fecha = models.DateField('Fecha de tramite', blank=True, null=True)
    impuesto = models.FloatField('Impuesto', blank=True, null=True)
    interes = models.FloatField('Interes', blank=True, null=True)
    multa = models.FloatField('Multa', blank=True, null=True)
    servicios_administrativos = models.FloatField('Servicios administrativos', blank=True, null=True)
    patente = models.ForeignKey(Patente, on_delete=models.CASCADE)

    def to_json(self):
        item = model_to_dict(self)
        return item

    class Meta:
        db_table = "detalle_patente"
