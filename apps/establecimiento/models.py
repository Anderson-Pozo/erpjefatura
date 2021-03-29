from django.db import models
from django.forms import model_to_dict
from apps.direccion.models import Direccion
from apps.auditoria.mixins import AuditMixin


# Create your models here.
ACTIVIDAD = (
    ('Comercial', 'Comercial'),
    ('Industrial', 'Industrial'),
    ('Inmobiliaria', 'Inmobiliaria'),
    ('Financiera', 'Financiera'),
    ('Artesanal', 'Artesanal'),
    ('Profesional', 'Profesional'),
    ('Alcoholes', 'Alcoholes'),
)


class TipoActividad(AuditMixin, models.Model):
    """
    Clase que representa la entidad Tipo Actividad que contiene
    la información del tipo de actividad comercial que realiza
    el negocio
    """
    id = models.AutoField(primary_key=True)
    tipo_actividad = models.CharField(
        'Tipo de actividad comercial',
        max_length=25,
        blank=False,
        null=True,
        choices=ACTIVIDAD
    )

    def __str__(self):
        return self.tipo_actividad

    class Meta:
        db_table = "tipo_actividad"


TIPO_VENTA = (
    ('Venta al por mayor', 'Venta al por mayor '),
    ('Venta al por menor', 'Venta al por menor '),
    ('Venta al por mayor y menor', 'Venta al por mayor y menor'),
)
SITUACION_LEGAL = (
    ('Propio', 'Propio'),
    ('Arrendado', 'Arrendado'),
    ('Anticresis', 'Anticresis'),
)


class Establecimiento(AuditMixin, models.Model):
    """
    Clase Establecimiento que almacena la información de los negocios que poseen
    una patente municipal
    """
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre del establecimiento', max_length=70, blank=False, null=True)
    descripcion_actividad = models.TextField('Descripcion actividad comercial', max_length=300, blank=True, null=True)
    fecha_inicio_actividad = models.DateField('Fecha de inicio de actividad comercial', blank=False, null=True)
    total_patrimonio = models.DecimalField(
        'Total de patrimonio',
        decimal_places=2,
        default=0.00,
        max_digits=10,
        blank=False,
        null=True
    )
    tipo_venta = models.CharField('Tipo de venta', max_length=35, blank=False, null=True, choices=TIPO_VENTA)
    estado = models.BooleanField('Activo/Inactivo', blank=True, null=True, default=True)
    situacion_legal = models.CharField('Situación legal', max_length=15, blank=True, null=True, choices=SITUACION_LEGAL)
    tipo_actividad = models.ForeignKey(TipoActividad, on_delete=models.CASCADE)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    def to_json(self):
        item = model_to_dict(self)
        item['nombre'] = self.nombre.title()
        item['tipo_actividad'] = self.tipo_actividad.tipo_actividad
        item['direccion'] = self.direccion.get_all_direccion()
        return item

    class Meta:
        db_table = "establecimiento"
