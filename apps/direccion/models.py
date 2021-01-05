from django.db import models


# Create your models here.
class Parroquia(models.Model):
    """
    Clase Parroquia  que almacena el nombre de la parroquia
    """
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre de la parroquia', max_length=20, blank=True, null=True)

    class Meta:
        db_table = "parroquia"


class Barrio(models.Model):
    """
    Clase Barrio almacena el nombre, la zona (Rural, Urbana), y su relacion con la
    tabla de parroquia
    """
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre del barrio', max_length=25, blank=True, null=True)
    zona = models.CharField('Zona', max_length=6, blank=True, null=True)
    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE)

    class Meta:
        db_table = "barrio"


class Direccion(models.Model):
    """
    Clase Direccion almacena la calle principal y secundaria, y su relacion con la
    tabla de Barrio
    """
    id = models.AutoField(primary_key=True)
    calle_principal = models.CharField('Calle Principal', max_length=35, blank=True, null=True)
    calle_secundaria = models.CharField('Calle Secundaria', max_length=35, blank=True, null=True)
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE)

    class Meta:
        db_table = "direccion"
