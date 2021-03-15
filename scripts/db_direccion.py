import os
from datetime import date
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erpjefatura.settings')
django.setup()

from apps.direccion.models import Parroquia

parroquias = [
    ['Huaca'],
    ['Mariscal Sucre'],
]


def db_parroquia():
    if Parroquia.objects.all().count() == 0:
        for i in parroquias:
            Parroquia.objects.create(
                nombre=i[0],
            )
        print('Script Parroquia ejecutado ...')
    else:
        print('Ya hay registros en Parroquia')

