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
    digito = models.IntegerField('Noveno dígito de cédula', blank=True, null=True)
    no_obligado = models.DateField('No obligado', blank=True, null=True)
    obligado = models.DateField('Obligado', blank=True, null=True)

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
    numero = models.IntegerField('Numero', blank=True, null=True)
    fraccion_basica = models.IntegerField('Fraccion basica', blank=True, null=True)
    fraccion_excedente = models.IntegerField('Fraccion excedente', blank=True, null=True)
    impuesto_fraccion_basica = models.IntegerField('Impuesto fraccion basica', blank=True, null=True)
    porcentaje_fraccion_excedente = models.FloatField('Porcentaje fraccion excedente', blank=True, null=True)

    def to_json(self):
        item = model_to_dict(self)
        return item

    class Meta:
        db_table = "impuesto"


class Multa(models.Model):
    """
    Modelo Multa que contiene los porcentajes de mmulta de mora por cada mes del año
    """
    id = models.AutoField(primary_key=True)
    anio = models.CharField('Año', max_length=4, blank=True, null=True)
    mes = models.CharField('Mes', max_length=15, blank=True, null=True)
    porcentaje = models.FloatField('Porcentaje multa', blank=True, null=True)

    def to_json(self):
        item = model_to_dict(self)
        return item

    class Meta:
        db_table = "multa"
