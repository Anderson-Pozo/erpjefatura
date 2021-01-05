# Generated by Django 3.0.2 on 2021-01-05 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('direccion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Predio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('clave_catastral', models.CharField(blank=True, max_length=25, null=True, verbose_name='Clave catastral')),
                ('avaluo_comercial', models.FloatField(blank=True, null=True, verbose_name='Avaluo comercial')),
                ('area_terreno', models.FloatField(blank=True, null=True, verbose_name='Área del terreno')),
                ('zona', models.CharField(blank=True, max_length=20, null=True, verbose_name='Zona urbana o rural')),
                ('direccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='direccion.Direccion')),
            ],
        ),
    ]
