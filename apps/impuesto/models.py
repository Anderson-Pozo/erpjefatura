from _ast import mod
from django.forms import model_to_dict
from django.db import models


# Create your models here.
class Vencimiento(models.Model):
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


class Impuesto(models.Model):
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
    porcentaje_fraccion_excedente = models.FloatField('Porcentaje fraccion excedente', blank=False, null=True)
    estado = models.BooleanField('Activo/Inactivo', blank=True, null=True, default=True)

    def to_json(self):
        item = model_to_dict(self)
        return item

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



class Multa(models.Model):
    """
    Modelo Multa que contiene los porcentajes de mmulta de mora por cada mes del año
    """
    id = models.AutoField(primary_key=True)
    fecha = models.DateField('Fecha', blank=False, null=True)
    # anio = models.CharField('Año', max_length=4, blank=False, null=True)
    # mes = models.CharField('Mes', max_length=15, blank=False, null=True, choices=MESES)
    porcentaje = models.FloatField('Porcentaje multa', blank=False, null=True)
    estado = models.BooleanField('Activo/Inactivo', blank=True, null=True, default=True)

    def to_json(self):
        item = model_to_dict(self)
        return item

    class Meta:
        db_table = "multa"
