from django.db import models
from django.forms import model_to_dict
from apps.auditoria.mixins import AuditMixin
from apps.impuesto.models import get_date_digito
from apps.usuario.models import User


OPCIONES_TIPO = (
    ('Natural', 'Natural'),
    ('Jurídica', 'Jurídica'),
)


class TipoContribuyente(AuditMixin, models.Model):
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


NACIONALIDADES = (
    ('Ecuatoriana', 'Ecuatoriana'),
    ('Colombiana', 'Colombiana'),
)


class Contribuyente(models.Model):
    """
    Clase Contribuyente almacena los datos informativos del contribuyente, y su relacion con la tabla
    TipoContribuyente
    """
    id = models.AutoField(primary_key=True)
    ruc = models.CharField('Ruc ', max_length=13, blank=False, null=True, unique=True)
    email = models.EmailField('Email', max_length=50, blank=True, null=True)
    nacionalidad = models.CharField('Nacionalidad', max_length=20, blank=True, null=True, choices=NACIONALIDADES)
    tlf_celular = models.CharField('Celular', max_length=10, blank=True, null=True)
    tlf_convencional = models.CharField('Telefono convencional', max_length=10, blank=True, null=True)
    estado = models.BooleanField('Activo/Inactivo', blank=True, null=True, default=True)
    tipocontribuyente = models.ForeignKey(TipoContribuyente, on_delete=models.CASCADE)

    def to_json(self):
        item = model_to_dict(self)
        item['tipocontribuyente'] = self.tipocontribuyente.nombre
        return item

    def __str__(self):
        return self.ruc

    def get_nombre(self):
        if self.tipocontribuyente.id == 1:
            return Natural.objects.get(ruc=self.ruc).__str__()
        else:
            return Juridico.objects.get(ruc=self.ruc).__str__()

    def get_fecha_vencimiento(self):
        return get_date_digito(self.ruc[8], self.tipocontribuyente.obligado_contabilidad)

    class Meta:
        db_table = "contribuyente"


class Natural(AuditMixin, Contribuyente):
    numero_cedula = models.CharField('Número de cédula', max_length=10, blank=False, null=True, unique=True)
    nombres = models.CharField('Nombres', max_length=50, blank=False, null=True)
    apellidos = models.CharField('Apellidos', max_length=50, blank=False, null=True)
    adulto = models.BooleanField('Tercera edad', blank=True, null=True, default=False)
    artesano = models.BooleanField('Artesano', blank=True, null=True, default=False)

    def __str__(self):
        return '{} {}'.format(self.nombres, self.apellidos)


class Juridico(AuditMixin, Contribuyente):
    razon_social = models.CharField('Razon social', max_length=50, blank=False, null=True)
    cedula_representante = models.CharField('Cédula del representante', max_length=10, blank=False, null=True)
    nombres_representante = models.CharField('Nombres del representante', max_length=50, blank=False, null=True)
    apellidos_representante = models.CharField('Apellidos del representante', max_length=50, blank=False, null=True)
    telefono_representante = models.CharField('Teléfono del representante', max_length=10, blank=True, null=True)
    correo_representante = models.EmailField('Correo del representante', max_length=50, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.razon_social)
