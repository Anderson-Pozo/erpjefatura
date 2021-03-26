from django.db import models
from django.forms import model_to_dict
from apps.auditoria.mixins import AuditMixin
from apps.direccion.models import Direccion


class Persona(AuditMixin, models.Model):
    id = models.AutoField(primary_key=True)
    numero_cedula = models.CharField('Número de cédula', max_length=10, blank=True, null=True, unique=True)
    nombres = models.CharField('Nombres', max_length=50, blank=True, null=True)
    apellidos = models.CharField('Apellidos', max_length=50, blank=True, null=True)
    casado = models.BooleanField('Casado', default=False, blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.nombres, self.apellidos)

    def get_nombres(self):
        return '{} {}'.format(self.nombres, self.apellidos)

    class Meta:
        db_table = "persona"

    def to_json(self):
        item = model_to_dict(self)
        return item


class Predio(AuditMixin, models.Model):
    """
    Clase Predio que contiene los campos de la entidad
    Predio y su relación con dirección
    """
    id = models.AutoField(primary_key=True)
    clave_catastral = models.CharField('Clave catastral', max_length=25, blank=True, null=True)
    avaluo_comercial = models.FloatField('Avaluo comercial', blank=True, null=True)
    area_terreno = models.FloatField('Área del terreno', blank=True, null=True)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)

    def get_zona(self):
        zona = self.direccion.barrio.zona
        return zona

    def __str__(self):
        return self.clave_catastral

    def to_json(self):
        item = model_to_dict(self)
        item['zona'] = self.get_zona()
        return item

    class Meta:
        db_table = "predio"


class Alcabala(AuditMixin, models.Model):
    """
    Clase Alcabala permite almacenar la información de la patente como la fecha, numero y tramite, ademas de los
    impuestos y valores que se calcularan para generar la alcabala, y su relacion con las tablas de comprador y
    vendedor.
    """
    id = models.AutoField(primary_key=True)
    fecha = models.DateField('Fecha', blank=True, null=True)
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
    comprador = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='comprador')
    vendedor = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='vendedor')
    predio = models.ForeignKey(Predio, on_delete=models.CASCADE)

    def get_total(self):
        total = self.impuesto_alcabalas + self.alcabalas_provinciales + \
               self.fondos_escolares + self.fondos_prevencion_riesgos + self.agua_potable
        return format(total, '.2f')

    def get_zona(self):
        zona = self.predio.direccion.barrio.zona
        return zona

    def get_valor_compra(self):
        return format(self.valor_compra_venta, '.2f')

    def to_json(self):
        item = model_to_dict(self)
        item['comprador'] = '{} {}'.format(self.comprador.nombres, self.comprador.apellidos)
        item['vendedor'] = '{} {}'.format(self.vendedor.nombres, self.vendedor.apellidos)
        item['predio'] = self.predio.clave_catastral
        item['total'] = self.get_total()
        return item

    class Meta:
        db_table = "alcabala"
