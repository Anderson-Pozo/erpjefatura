from _ast import mod
from django.forms import model_to_dict
from django.db import models
from apps.auditoria.mixins import AuditMixin


# Create your models here.
class Vencimiento(AuditMixin, models.Model):
    """"
    Clase vencimiento que almacena las fechas de vencimiento de la multa
    dependiendo del noveno digito de cédula
    """
    id = models.AutoField(primary_key=True)
    digito = models.IntegerField('Noveno dígito de cédula', blank=False, null=True)
    no_obligado = models.DateField('No obligado', blank=False, null=True)
    obligado = models.DateField('Obligado', blank=False, null=True)
    estado = models.BooleanField('Activo/Inactivo', blank=True, null=True, default=True)

    def to_json(self):
        item = model_to_dict(self)
        return item

    class Meta:
        db_table = "vencimiento"


class Impuesto(AuditMixin, models.Model):
    """
    Clase impuesto que almacena valores correspondientes a las
    fracciones basicas y excedentes para calcular el valor del
    impuesto de la patente
    """
    id = models.AutoField(primary_key=True)
    numero = models.IntegerField('Numero', blank=False, null=True)
    fraccion_basica = models.IntegerField('Fraccion basica', blank=False, null=True)
    fraccion_excedente = models.IntegerField('Fraccion excedente', blank=False, null=True)
    impuesto_fraccion_basica = models.IntegerField('Impuesto fraccion basica', blank=False, null=True)
    porcentaje_fraccion_excedente = models.DecimalField(
        'Porcentaje fraccion excedente',
        decimal_places=3,
        default=0.000,
        max_digits=9,
        blank=False,
        null=True
    )
    estado = models.BooleanField('Activo/Inactivo', blank=True, null=True, default=True)

    def to_json(self):
        item = model_to_dict(self)
        return item

    def calcular_impuesto(self, capital):
        if 0 <= capital <= 600:
            return 0
        if 600 <= capital <= 800:
            return 600
        if 800 <= capital <= 1000:
            return 800
        if 1000 <= capital <= 1200:
            return 1000
        if 1200 <= capital <= 1500:
            return 1200
        if 1500 <= capital <= 3000:
            return 1500
        if capital > self.fraccion_basica:
            return 'Es mayor'
        else:
            return 'Es menor'

    class Meta:
        db_table = "impuesto"


MESES = (
    ('Enero', 'Enero'),
    ('Febrero', 'Febrero'),
    ('Marzo', 'Marzo'),
    ('Abril', 'Abril'),
    ('Mayo', 'Mayo'),
    ('Junio', 'Junio'),
    ('Julio', 'Julio'),
    ('Agosto', 'Agosto'),
    ('Septiembre', 'Septiembre'),
    ('Octubre', 'Octubre'),
    ('Noviembre', 'Noviembre'),
    ('Diciembre', 'Diciembre'),
)


class Multa(AuditMixin, models.Model):
    """
    Modelo Multa que contiene los porcentajes de mmulta de mora por cada mes del año
    """
    id = models.AutoField(primary_key=True)
    fecha = models.DateField('Fecha', blank=False, null=True)
    porcentaje = models.DecimalField(
        'Porcentaje multa',
        decimal_places=5,
        default=0.00000,
        max_digits=9,
        blank=False,
        null=True
    )
    estado = models.BooleanField('Activo/Inactivo', blank=True, null=True, default=True)

    def to_json(self):
        item = model_to_dict(self)
        return item

    class Meta:
        db_table = "multa"
