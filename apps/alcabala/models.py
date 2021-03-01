from django.db import models
from django.forms import model_to_dict
from apps.predio.models import Predio
from apps.auditoria.mixins import AuditMixin


# Create your models here.
class Comprador(AuditMixin, models.Model):
    """
    Clase Comprador permite guardar la información de numero de cédula, nombres, apellidos, casado del comprador
    """
    id = models.AutoField(primary_key=True)
    numero_cedula = models.CharField('Número de cédula comprador', max_length=10, blank=True, null=True)
    nombres = models.CharField('Nombres', max_length=50, blank=True, null=True)
    apellidos = models.CharField('Apellidos', max_length=50, blank=True, null=True)
    casado = models.BooleanField('Casado', default=False, blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.nombres, self.apellidos)

    def get_nombres(self):
        return '{} {}'.format(self.nombres, self.apellidos)

    class Meta:
        db_table = "comprador"

    # def __str__(self):
    #     return self.nombres + ' ' + self.apellidos

    def to_json(self):
        item = model_to_dict(self)
        return item


class Vendedor(AuditMixin, models.Model):
    """
    Clase Vendedor permite guardar la información de numero de cédula, nombres, apellidos, casado del vendedor
    """
    id = models.AutoField(primary_key=True)
    numero_cedula = models.CharField('Número de cédula vendedor', max_length=10, blank=True, null=True)
    nombres = models.CharField('Nombres', max_length=50, blank=True, null=True)
    apellidos = models.CharField('Apellidos', max_length=50, blank=True, null=True)
    casado = models.BooleanField('Casado', default=False, blank=True, null=True)

    class Meta:
        db_table = "vendedor"

    def __str__(self):
        return '{} {}'.format(self.nombres, self.apellidos)

    def get_nombres(self):
        return '{} {}'.format(self.nombres, self.apellidos)

    # def __str__(self):
    #     return self.nombres + ' ' + self.apellidos

    def to_json(self):
        item = model_to_dict(self)
        return item


class Alcabala(AuditMixin, models.Model):
    """
    Clase Alcabala permite almacenar la información de la patente como la fecha, numero y tramite, ademas de los
    impuestos y valores que se calcularan para generar la alcabala, y su relacion con las tablas de comprador y
    vendedor.
    """
    id = models.AutoField(primary_key=True)
    fecha = models.DateField('Fecha', blank=True, null=True)
    # numero = models.IntegerField('Numero', blank=True, null=True)
    descripcion_tramite = models.TextField('Descripcion del tramite', max_length=300, blank=True, null=True)
    valor_compra_venta = models.DecimalField(
        'Valor de la compra-venta',
        decimal_places=2,
        default=0.00,
        max_digits=9,
        blank=False,
        null=True
    )
    impuesto_alcabalas = models.DecimalField(
        'Impuesto de alacabalas',
        decimal_places=2,
        default=0.00,
        max_digits=9,
        blank=False,
        null=True
    )
    alcabalas_provinciales = models.DecimalField(
        'Alcabalas provinciales',
        decimal_places=2,
        default=0.00,
        max_digits=9,
        blank=False,
        null=True
    )
    fondos_escolares = models.DecimalField(
        'Fondos escolares',
        decimal_places=2,
        default=0.00,
        max_digits=9,
        blank=False,
        null=True
    )
    fondos_prevencion_riesgos = models.DecimalField(
        'Fondos de prevencion de riesgos',
        decimal_places=2,
        default=0.00,
        max_digits=9,
        blank=False,
        null=True
    )
    agua_potable = models.DecimalField(
        'Agua potable',
        decimal_places=2,
        default=0.00,
        max_digits=9,
        blank=False,
        null=True
    )
    comprador = models.ForeignKey(Comprador, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    predio = models.ForeignKey(Predio, on_delete=models.CASCADE)

    def get_total(self):
        total = self.impuesto_alcabalas + self.alcabalas_provinciales + \
               self.fondos_escolares + self.fondos_prevencion_riesgos + self.agua_potable
        return format(total, '.2f')

    def to_json(self):
        item = model_to_dict(self)
        item['comprador'] = '{} {}'.format(self.comprador.nombres, self.comprador.apellidos)
        item['vendedor'] = '{} {}'.format(self.vendedor.nombres, self.vendedor.apellidos)
        item['predio'] = self.predio.clave_catastral
        return item

    class Meta:
        db_table = "alcabala"
