from django.db import models
from apps.direccion.models import Direccion


# Create your models here.
class TipoActividad(models.Model):
    """
    Clase que representa la entidad Tipo Actividad que contiene
    la información del tipo de actividad comercial que realiza
    el negocio
    """
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Tipo de actividad comercial', max_length=25, blank=True, null=True)


class Establecimiento(models.Model):
    """
    Clase Establecimiento que almacena la información de los negocios que poseen
    una patente municipal
    """
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre del establecimiento', max_length=50, blank=True, null=True)
    descripcion_actividad = models.TextField('Descripcion actividad comercial', max_length=300, blank=True, null=True)
    fecha_inicio_actividad = models.DateField('Fecha de inicio de actividad comercial', blank=True, null=True)
    total_patrimonio = models.FloatField('Total de patrimonio', blank=True, null=True)
    tipo_actividad = models.ForeignKey(TipoActividad, on_delete=models.CASCADE)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
