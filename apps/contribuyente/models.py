from django.db import models


# Create your models here.
class TipoContribuyente(models.Model):
    """
    Clase Tipo Contribuyente que almacena el nombre del contribuyente (natural o juridico), y si este es obligado
    a llevar contabilidad
    """
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Tipo de contribuyente ', max_length=20, blank=True, null=True)
    obligado_contabilidad = models.BooleanField('Obligado a llevar contabilidad ', default=False, blank=True, null=True)

    class Meta:
        db_table = "tipo_contribuyente"


class Contribuyente(models.Model):
    """
    Clase Contribuyente almacena los datos informativos del contribuyente, y su relacion con la tabla
    TipoContribuyente
    """
    id = models.AutoField(primary_key=True)
    ruc = models.CharField('Ruc ', max_length=13, blank=True, null=True)
    numero_cedula = models.CharField('Número de cédula', max_length=10, blank=True, null=True)
    nacionalidad = models.CharField('Nacionalidad', max_length=20, blank=True, null=True)
    nombres = models.CharField('Nombres', max_length=50, blank=True, null=True)
    apellidos = models.CharField('Apellidos', max_length=50, blank=True, null=True)
    email = models.CharField('Email', max_length=50, blank=True, null=True)
    tlf_celular = models.CharField('Celular', max_length=10, blank=True, null=True)
    tlf_convencional = models.CharField('Telefono convencional', max_length=10, blank=True, null=True)
    tipocontribuyente = models.ForeignKey(TipoContribuyente, on_delete=models.CASCADE)

    class Meta:
        db_table = "contribuyente"
