import os
from datetime import date
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erpjefatura.settings')
django.setup()

from apps.direccion.models import Parroquia, Barrio, Direccion

parroquias = [
    ['Huaca'],
    ['Mariscal Sucre'],
]

barrios = [
    ['Centro', 'Urbana', 1],
    ['Norte', 'Urbana', 1],
    ['Sur', 'Urbana', 1],
    ['Olivos', 'Urbana', 1],
    ['La Calera', 'Urbana', 1],
    ['01 de Mayo', 'Urbana', 1],
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


def db_barrio():
    parroq1 = Parroquia.objects.get(id=1)
    if Barrio.objects.all().count() == 0:
        for i in barrios:
            Barrio.objects.create(
                nombre=i[0],
                zona=i[1],
                parroquia=parroq1
            )
        print('Script Barrio ejecutado ...')
    else:
        print('Ya hay registros en Barrio')
