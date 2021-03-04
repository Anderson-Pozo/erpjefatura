from django.db import models
from django.forms import model_to_dict
from apps.patente.models import *
from apps.impuesto.models import *
from apps.establecimiento.models import *
from apps.auditoria.mixins import AuditMixin


class VistaUsuario(AuditMixin, models.Model):

    def to_json(self):
        item = model_to_dict(self)
        item['fecha'] =  DetallePatente.fecha
        item['impuesto'] = DetallePatente.impuesto
        item['interes'] = DetallePatente.interes
        item['multa'] = DetallePatente.multa
        item['servicios'] = DetallePatente.servicios_administrativos
        return item

    def get_fecha(self):
        fecha_ultimo_pago(self.id)

    def get_perfil(self):
            Contribuyente.ruc(self.id)

    def get_establecimientos(self):
             Establecimiento.nombre(self.id)

    class Meta:
        db_table = "VistaUsuario"