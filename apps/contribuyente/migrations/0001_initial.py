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
            name='Contribuyente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ruc', models.CharField(max_length=13, null=True, unique=True, verbose_name='Ruc ')),
                ('email', models.EmailField(blank=True, max_length=50, null=True, verbose_name='Email')),
                ('nacionalidad', models.CharField(blank=True, choices=[('Ecuatoriana', 'Ecuatoriana'), ('Colombiana', 'Colombiana')], max_length=20, null=True, verbose_name='Nacionalidad')),
                ('tlf_celular', models.CharField(blank=True, max_length=10, null=True, verbose_name='Celular')),
                ('tlf_convencional', models.CharField(blank=True, max_length=10, null=True, verbose_name='Telefono convencional')),
                ('estado', models.BooleanField(blank=True, default=True, null=True, verbose_name='Activo/Inactivo')),
            ],
            options={
                'db_table': 'contribuyente',
            },
        ),
        migrations.CreateModel(
            name='TipoContribuyente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, choices=[('Natural', 'Natural'), ('Jurídica', 'Jurídica')], max_length=20, null=True, verbose_name='Tipo de contribuyente ')),
                ('obligado_contabilidad', models.BooleanField(blank=True, default=False, null=True, verbose_name='Obligado a llevar contabilidad ')),
            ],
            options={
                'db_table': 'tipo_contribuyente',
            },
            bases=(apps.auditoria.mixins.AuditMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Juridico',
            fields=[
                ('contribuyente_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='contribuyente.Contribuyente')),
                ('razon_social', models.CharField(max_length=70, null=True, verbose_name='Razon social')),
                ('cedula_representante', models.CharField(max_length=10, null=True, verbose_name='Cédula del representante')),
                ('nombres_representante', models.CharField(max_length=50, null=True, verbose_name='Nombres del representante')),
                ('apellidos_representante', models.CharField(max_length=50, null=True, verbose_name='Apellidos del representante')),
                ('telefono_representante', models.CharField(blank=True, max_length=10, null=True, verbose_name='Teléfono del representante')),
                ('correo_representante', models.EmailField(blank=True, max_length=50, null=True, verbose_name='Correo del representante')),
            ],
            bases=(apps.auditoria.mixins.AuditMixin, 'contribuyente.contribuyente'),
        ),
        migrations.CreateModel(
            name='Natural',
            fields=[
                ('contribuyente_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='contribuyente.Contribuyente')),
                ('numero_cedula', models.CharField(max_length=10, null=True, unique=True, verbose_name='Número de cédula')),
                ('nombres', models.CharField(max_length=50, null=True, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=50, null=True, verbose_name='Apellidos')),
                ('adulto', models.BooleanField(blank=True, default=False, null=True, verbose_name='Tercera edad')),
                ('artesano', models.BooleanField(blank=True, default=False, null=True, verbose_name='Artesano')),
            ],
            bases=(apps.auditoria.mixins.AuditMixin, 'contribuyente.contribuyente'),
        ),
        migrations.AddField(
            model_name='contribuyente',
            name='tipocontribuyente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contribuyente.TipoContribuyente'),
        ),
    ]