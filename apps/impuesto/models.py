from django.db import models


# Create your models here.
class Vencimiento(models.Model):
    id = models.AutoField(primary_key=True)
    digito = models.IntegerField('Noveno dígito de cédula', blank=True, null=True)
    no_obligado = models.DateField('No obligado', blank=True, null=True)
    obligado = models.DateField('Obligado', blank=True, null=True)


class Impuesto(models.Model):
    id = models.AutoField(primary_key=True)
    numero = models.IntegerField('Numero', blank=True, null=True)
    fraccion_basica = models.IntegerField('Fraccion basica', blank=True, null=True)
    fraccion_excedente = models.IntegerField('Fraccion excedente', blank=True, null=True)
    impuesto_fraccion_basica = models.IntegerField('Impuesto fraccion basica', blank=True, null=True)
    porcentaje_fraccion_excedente = models.FloatField('Porcentaje fraccion excedente', blank=True, null=True)
