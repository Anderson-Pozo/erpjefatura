from django.db import models
from django.db.models import Q
from django.forms import model_to_dict
from apps.auditoria.mixins import AuditMixin
from apps.impuesto.models import get_date_digito
from django.db.models.signals import post_save
from apps.usuario.models import User
from apps.administrador.models import send_mail_fun, send_mail_thread


# Create your models here.

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


class Contribuyente(models.Model):
    """
    Clase Contribuyente almacena los datos informativos del contribuyente, y su relacion con la tabla
    TipoContribuyente
    """
    id = models.AutoField(primary_key=True)
    ruc = models.CharField('Ruc ', max_length=13, blank=False, null=True, unique=True)
    email = models.EmailField('Email', max_length=50, blank=True, null=True)
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

    def get_nombre(self, ruc):
        if self.tipocontribuyente.id == 1:
            return Natural.objects.get(ruc=ruc).get_nombre()
        else:
            return Juridico.objects.get(ruc=ruc).get_nombre()

    def get_fecha_vencimiento(self):
        return get_date_digito(self.ruc[8], self.tipocontribuyente.obligado_contabilidad)

    class Meta:
        db_table = "contribuyente"


NACIONALIDADES = (
    ('Ecuatoriana', 'Ecuatoriana'),
    ('Colombiana', 'Colombiana'),
)


class Natural(AuditMixin, Contribuyente):
    numero_cedula = models.CharField('Número de cédula', max_length=10, blank=False, null=True, unique=True)
    nacionalidad = models.CharField('Nacionalidad', max_length=20, blank=True, null=True, choices=NACIONALIDADES)
    nombres = models.CharField('Nombres', max_length=50, blank=False, null=True)
    apellidos = models.CharField('Apellidos', max_length=50, blank=False, null=True)
    adulto = models.BooleanField('Tercera edad', blank=True, null=True, default=False)
    artesano = models.BooleanField('Artesano', blank=True, null=True, default=False)

    def get_nombre(self):
        return '{} {}'.format(self.nombres, self.apellidos)

    def __str__(self):
        return '{} {}'.format(self.nombres, self.apellidos)


class Juridico(AuditMixin, Contribuyente):
    razon_social = models.CharField('Razon social', max_length=50, blank=False, null=True)
    cedula_representante = models.CharField('Cédula del representante', max_length=10, blank=False, null=True)
    nombres_representante = models.CharField('Nombres del representante', max_length=50, blank=False, null=True)
    apellidos_representante = models.CharField('Apellidos del representante', max_length=50, blank=False, null=True)
    telefono_representante = models.CharField('Teléfono del representante', max_length=10, blank=True, null=True)
    correo_representante = models.EmailField('Correo del representante', max_length=50, blank=True, null=True)

    def get_nombre(self):
        return '{}'.format(self.razon_social)

    def __str__(self):
        return '{}'.format(self.razon_social)


def generate_user_natural(sender, instance, **kwargs):
    try:
        row = User.objects.filter(
            Q(username=instance.numero_cedula) |
            Q(email=instance.email)).count()

        if row == 0:
            new_user = User(
                email=instance.email,
                username=instance.numero_cedula,
                first_name=instance.nombres,
                last_name=instance.apellidos,
                is_superuser=False,
                is_active=True,
            )
            new_user.set_password(instance.numero_cedula)
            new_user.save()
            # send_mail_thread(instance.email, 1, {'user': instance.nombres + ' ' + instance.apellidos})
        else:
            pass
    except Exception as error:
        print(error)


def generate_user_juridico(sender, instance, **kwargs):
    try:
        row = User.objects.filter(
            Q(username=instance.cedula_representante) |
            Q(email=instance.email)).count()

        if row == 0:
            new_user = User(
                email=instance.email,
                username=instance.cedula_representante,
                first_name=instance.razon_social,
                last_name='',
                is_superuser=False,
                is_active=True,
            )
            new_user.set_password(instance.cedula_representante)
            new_user.save()
        else:
            pass
    except Exception as error:
        print(error)


# post_save.connect(generate_user_natural, sender=Natural)
# post_save.connect(generate_user_juridico, sender=Juridico)
