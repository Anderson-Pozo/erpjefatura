from django.db import models
from django.forms import model_to_dict


# Create your models here.

OPCIONES_TIPO = (
    ('NATURAL', 'Natural'),
    ('JURIDICA', 'Jurídica'),
)


class TipoContribuyente(models.Model):
    """
    Clase Tipo Contribuyente que almacena el nombre del contribuyente (natural o juridico), y si este es obligado
    a llevar contabilidad
    """
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Tipo de contribuyente ', max_length=20, blank=True, null=True, choices=OPCIONES_TIPO)
    obligado_contabilidad = models.BooleanField('Obligado a llevar contabilidad ', default=False, blank=True, null=True)

    # def natural_key(self):
    #     return self.nombre

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "tipo_contribuyente"


class Contribuyente(models.Model):
    """
    Clase Contribuyente almacena los datos informativos del contribuyente, y su relacion con la tabla
    TipoContribuyente
    """
    id = models.AutoField(primary_key=True)
    ruc = models.CharField('Ruc ', max_length=13, blank=False, null=True, unique=True)
    numero_cedula = models.CharField('Número de cédula', max_length=10, blank=False, null=True, unique=True)
    nacionalidad = models.CharField('Nacionalidad', max_length=20, blank=True, null=True)
    nombres = models.CharField('Nombres', max_length=50, blank=False, null=True)
    apellidos = models.CharField('Apellidos', max_length=50, blank=False, null=True)
    email = models.CharField('Email', max_length=50, blank=True, null=True)
    tlf_celular = models.CharField('Celular', max_length=10, blank=True, null=True)
    tlf_convencional = models.CharField('Telefono convencional', max_length=10, blank=True, null=True)
    tipocontribuyente = models.ForeignKey(TipoContribuyente, on_delete=models.CASCADE)

    def to_json(self):
        item = model_to_dict(self)
        item['tipocontribuyente'] = self.tipocontribuyente.nombre
        return item

    def __str__(self):
        return self.nombres

    class Meta:
        db_table = "contribuyente"


class Sociedad(Contribuyente):
    razon_social = models.CharField('Razon social', max_length=10, blank=False, null=True)

    # class Meta:
    #     db_table = 'sociedad'
