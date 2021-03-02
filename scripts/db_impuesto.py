import os
from datetime import date

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erpjefatura.settings')
django.setup()

from apps.impuesto.models import Vencimiento, Impuesto, Multa


vencimiento = [
    [1, date(2015, 4, 10), date(2015, 5, 10)],
    [2, date(2015, 4, 12), date(2015, 5, 12)],
    [3, date(2015, 4, 14), date(2015, 5, 14)],
    [4, date(2015, 4, 16), date(2015, 5, 16)],
    [5, date(2015, 4, 18), date(2015, 5, 18)],
    [6, date(2015, 4, 20), date(2015, 5, 20)],
    [7, date(2015, 4, 22), date(2015, 5, 22)],
    [8, date(2015, 4, 24), date(2015, 5, 24)],
    [9, date(2015, 4, 26), date(2015, 5, 26)],
    [0, date(2015, 4, 28), date(2015, 5, 28)],
]

impuestos = [
    [1, 0, 600, 10, 0.0],
    [2, 600, 800, 10, 0.03500],
    [3, 800, 1000, 17, 0.01502],
    [4, 1000, 1200, 20, 0.01000],
]


def db_vencimiento():
    for i in vencimiento:
        Vencimiento.objects.create(
            digito=i[0],
            obligado=i[1],
            no_obligado=i[2]
        )


def db_impuesto():
    for i in impuestos:
        Impuesto.objects.create(
            numero=i[0],
            fraccion_basica=i[1],
            fraccion_excedente=i[2],
            impuesto_fraccion_basica=i[3],
            porcentaje_fraccion_excedente=i[4]
        )
