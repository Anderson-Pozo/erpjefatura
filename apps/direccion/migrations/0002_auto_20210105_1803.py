# Generated by Django 3.0.2 on 2021-01-05 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('direccion', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='barrio',
            table='barrio',
        ),
        migrations.AlterModelTable(
            name='direccion',
            table='direccion',
        ),
        migrations.AlterModelTable(
            name='parroquia',
            table='parroquia',
        ),
    ]
