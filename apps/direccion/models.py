from django.db import models
from apps.auditoria.mixins import AuditMixin
from django.forms import model_to_dict


# Create your models here.
class Parroquia(AuditMixin, models.Model):
    """
    Clase Parroquia  que almacena el nombre de la parroquia
    """
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre de la parroquia', max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "parroquia"


ZONA = (
    ('Urbana', 'Urbana'),
    ('Rural', 'Rural')
)


class Barrio(AuditMixin, models.Model):
    """
    Clase Barrio almacena el nombre, la zona (Rural, Urbana), y su relacion con la
    tabla de parroquia
    """
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre del barrio', max_length=25, blank=True, null=True)
    zona = models.CharField('Zona', max_length=6, blank=True, null=True, choices=ZONA)
    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "barrio"


class Direccion(AuditMixin, models.Model):
    """
    Clase Direccion almacena la calle principal y secundaria, y su relacion con la
    tabla de Barrio
    """
    id = models.AutoField(primary_key=True)
    calle_principal = models.CharField('Calle Principal', max_length=35, blank=True, null=True)
    calle_secundaria = models.CharField('Calle Secundaria', max_length=35, blank=True, null=True)
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE)

    def __str__(self):
        return self.get_all_direccion()

    def get_all_direccion(self):
        return 'B. ' + self.barrio.nombre + ', cl. ' + self.calle_principal + ' y ' + self.calle_secundaria

    def get_select2(self):
        return '{}, B. {} cl. {} y {}'.format(
            self.barrio.parroquia.nombre,
            self.barrio.nombre,
            self.calle_principal,
            self.calle_secundaria
        )

    def to_json(self):
        item = model_to_dict(self)
        return item
    
    class Meta:
        db_table = "direccion"
