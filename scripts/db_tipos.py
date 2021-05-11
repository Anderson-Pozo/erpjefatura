import os
from datetime import date
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erpjefatura.settings.production')
django.setup()

from apps.contribuyente.models import TipoContribuyente
from apps.establecimiento.models import TipoActividad

tipos_contribuyente = [
    [1, 'Natural'], [2, 'Jurídica'],
]

tipos_actividad = [
    ['Comercial'], ['Industrial'], ['Inmobiliaria'],
    ['Financiera'], ['Artesanal'], ['Profesional'],
    ['Alcoholes']
]


def db_tipo_contribuyente():
    if TipoContribuyente.objects.all().count() == 0:
        for i in tipos_contribuyente:
            TipoContribuyente.objects.create(
                id=i[0],
                nombre=i[1]
            )
        print('Script Tipo Contribuyente ejecutado ...')
    else:
        print('Ya hay registros en Tipo Contribuyente')


def db_tipo_actividad():
    if TipoActividad.objects.all().count() == 0:
        for i in tipos_actividad:
            TipoActividad.objects.create(
                tipo_actividad=i[0]
            )
        print('Script Tipo Actividad ejecutado ...')
    else:
        print('Ya hay registros en Tipo Actividad')

