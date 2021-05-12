# Generated by Django 3.0.2 on 2021-05-11 15:48

import apps.auditoria.mixins
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barrio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=25, null=True, verbose_name='Nombre del barrio')),
                ('zona', models.CharField(blank=True, choices=[('Urbana', 'Urbana'), ('Rural', 'Rural')], max_length=6, null=True, verbose_name='Zona')),
            ],
            options={
                'db_table': 'barrio',
            },
            bases=(apps.auditoria.mixins.AuditMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Parroquia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=20, null=True, verbose_name='Nombre de la parroquia')),
            ],
            options={
                'db_table': 'parroquia',
            },
            bases=(apps.auditoria.mixins.AuditMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('calle_principal', models.CharField(blank=True, max_length=35, null=True, verbose_name='Calle Principal')),
                ('calle_secundaria', models.CharField(blank=True, max_length=35, null=True, verbose_name='Calle Secundaria')),
                ('barrio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='direccion.Barrio')),
            ],
            options={
                'db_table': 'direccion',
            },
            bases=(apps.auditoria.mixins.AuditMixin, models.Model),
        ),
        migrations.AddField(
            model_name='barrio',
            name='parroquia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='direccion.Parroquia'),
        ),
    ]