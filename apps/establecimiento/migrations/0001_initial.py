# Generated by Django 3.0.2 on 2021-01-07 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('direccion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoActividad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=25, null=True, verbose_name='Tipo de actividad comercial')),
            ],
            options={
                'db_table': 'tipo_actividad',
            },
        ),
        migrations.CreateModel(
            name='Establecimiento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nombre del establecimiento')),
                ('descripcion_actividad', models.TextField(blank=True, max_length=300, null=True, verbose_name='Descripcion actividad comercial')),
                ('fecha_inicio_actividad', models.DateField(blank=True, null=True, verbose_name='Fecha de inicio de actividad comercial')),
                ('total_patrimonio', models.FloatField(blank=True, null=True, verbose_name='Total de patrimonio')),
                ('direccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='direccion.Direccion')),
                ('tipo_actividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='establecimiento.TipoActividad')),
            ],
            options={
                'db_table': 'establecimiento',
            },
        ),
    ]