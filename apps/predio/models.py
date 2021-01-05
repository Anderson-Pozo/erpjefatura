from django.db import models
from apps.direccion.models import Direccion


# Create your models here.
class Predio(models.Model):
    """
    Clase Predio que contiene los campos de la entidad
    Predio y su relación con dirección
    """
    id = models.AutoField(primary_key=True)
    clave_catastral = models.CharField('Clave catastral', max_length=25, blank=True, null=True)
    avaluo_comercial = models.FloatField('Avaluo comercial', blank=True, null=True)
    area_terreno = models.FloatField('Área del terreno', blank=True, null=True)
    zona = models.CharField('Zona urbana o rural', max_length=20, blank=True, null=True)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
