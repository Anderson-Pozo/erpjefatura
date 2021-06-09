# Generated by Django 3.0.2 on 2021-05-11 15:48

import apps.auditoria.mixins
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('alcabala', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plusvalia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_tramite', models.DateField(blank=True, null=True, verbose_name='Fecha del tramite')),
                ('fecha_escritura', models.DateField(blank=True, null=True, verbose_name='Fecha de la escritura')),
                ('precio_venta', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, null=True, verbose_name='Precio de venta')),
                ('precio_adquisicion', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, null=True, verbose_name='Precio de adquisición')),
                ('diferencia_bruta', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, null=True, verbose_name='Diferencia bruta')),
                ('rebaja_mejoras', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, null=True, verbose_name='Rebaja por mejoras')),
                ('diferencia_neta', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, null=True, verbose_name='Diferencia neta')),
                ('tenencia', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, null=True, verbose_name='Tenencia')),
                ('base_rebajar_moneda', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, null=True, verbose_name='Base para rebajar moneda')),
                ('rebaja_desvalorizacion', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, null=True, verbose_name='Rebaja por desvalorización')),
                ('utilidad_imponible', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, null=True, verbose_name='Utilidad imponible')),
                ('alcabala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alcabala.Alcabala')),
            ],
            options={
                'db_table': 'plusvalia',
            },
            bases=(apps.auditoria.mixins.AuditMixin, models.Model),
        ),
    ]