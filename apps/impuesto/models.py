from _ast import mod
from django.forms import model_to_dict
from django.db import models
from apps.auditoria.mixins import AuditMixin
from apps.utils.calc_months import calcular_meses


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

    def __str__(self):
        return 'Digito cédula {}'.format(self.digito)

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
        decimal_places=5,
        default=0.000,
        max_digits=9,
        blank=False,
        null=True
    )
    estado = models.BooleanField('Activo/Inactivo', blank=True, null=True, default=True)

    def __str__(self):
        return '{}) {} - {}'.format(self.numero, self.fraccion_basica, self.fraccion_excedente)

    def to_json(self):
        item = model_to_dict(self)
        return item

    class Meta:
        db_table = "impuesto"


class Multa(AuditMixin, models.Model):
    """
    Modelo Multa que contiene los porcentajes de multa de mora por cada mes del año
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

    def __str__(self):
        return self.fecha.strftime('%d %B, %Y')

    def to_json(self):
        item = model_to_dict(self)
        return item

    class Meta:
        db_table = "multa"


def calcular_impuesto(capital):
    row = Impuesto.objects.get(fraccion_basica__lt=capital, fraccion_excedente__gte=capital)
    diferencia = capital - row.fraccion_basica
    suma = row.impuesto_fraccion_basica + (diferencia * row.porcentaje_fraccion_excedente)
    return format(suma, '.2f')


def get_date_digito(digito, obligado):
    if obligado:
        fecha = Vencimiento.objects.get(digito=digito).obligado
        return fecha
    else:
        fecha = Vencimiento.objects.get(digito=digito).no_obligado
        return fecha


def calc_meses_multa(fecha_vencimiento, fecha_actual):
    n_fechas = calcular_meses(fecha_vencimiento, fecha_actual)
    multas = Multa.objects.filter(fecha__range=(fecha_vencimiento, fecha_actual))[0:n_fechas]
    return multas
