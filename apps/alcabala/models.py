from django.db import models
from apps.predio.models import Predio

# Create your models here.
class Comprador(models.Model):
    """
    Clase Comprador permite guardar la información de numero de cédula, nombres, apellidos, casado del comprador
    """
    id = models.AutoField(primary_key=True)
    numero_cedula = models.CharField('Número de cédula comprador', max_length=10, blank=True, null=True)
    nombres = models.CharField('Nombres', max_length=50, blank=True, null=True)
    apellidos = models.CharField('Apellidos', max_length=50, blank=True, null=True)
    casado = models.BooleanField('Casado', default=False, blank=True, null=True)


class Vendedor(models.Model):
    """
    Clase Vendedor permite guardar la información de numero de cédula, nombres, apellidos, casado del vendedor
    """
    id = models.AutoField(primary_key=True)
    numero_cedula = models.CharField('Número de cédula vendedor', max_length=10, blank=True, null=True)
    nombres = models.CharField('Nombres', max_length=50, blank=True, null=True)
    apellidos = models.CharField('Apellidos', max_length=50, blank=True, null=True)
    casado = models.BooleanField('Casado', default=False, blank=True, null=True)


class Alcabala(models.Model):
    """
    Clase Alcabala permite almacenar la información de la patente como la fecha, numero y tramite, ademas de los
    impuestos y valores que se calcularan para generar la alcabala, y su relacion con las tablas de comprador y
    vendedor.
    """
    id = models.AutoField(primary_key=True)
    fecha = models.DateField('Fecha', blank=True, null=True)
    numero = models.IntegerField('Numero', blank=True, null=True)
    descripcion_tramite = models.TextField('Descripcion del tramite',max_length=300 , blank=True, null=True)
    valor_compra_venta = models.FloatField('Valor de la compra-venta', blank=True, null=True)
    impuesto_alcabalas = models.FloatField('Impuesto de alacabalas', blank=True, null=True)
    alcabalas_provinciales = models.FloatField('Alcabalas provinciales', blank=True, null=True)
    fondos_escolares = models.FloatField('Fondos escolares', blank=True, null=True)
    fondos_prevencion_riesgos = models.FloatField('Fondos de prevencion de riesgos', blank=True, null=True)
    agua_potable = models.FloatField('Agua potable', blank=True, null=True)
    comprador = models.ForeignKey(Comprador, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    predio = models.ForeignKey(Predio, on_delete=models.CASCADE)
