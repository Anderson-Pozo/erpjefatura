# Generated by Django 3.0.2 on 2021-05-11 15:48

import django.contrib.admin.models
from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logs',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('admin.logentry',),
            managers=[
                ('objects', django.contrib.admin.models.LogEntryManager()),
            ],
        ),
    ]
