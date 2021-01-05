# Generated by Django 3.0.2 on 2021-01-05 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('predio', '0001_initial'),
        ('alcabala', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alcabala',
            name='predio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='predio.Predio'),
        ),
        migrations.AddField(
            model_name='alcabala',
            name='vendedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alcabala.Vendedor'),
        ),
    ]
