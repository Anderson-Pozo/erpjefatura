from django.db import models


class Demo(models.Model):
    id = models.AutoField(primary_key=True)
    texto = models.CharField('Texto', blank=True, null=True, max_length=15)
