from datetime import date, datetime, timedelta
from django.db import models
from django.forms import model_to_dict
from django.utils.timezone import now
from apps.contribuyente.models import Contribuyente
from apps.establecimiento.models import Establecimiento
from apps.impuesto.models import Impuesto, calcular_impuesto, calc_meses_multa
from apps.auditoria.mixins import AuditMixin

from apps.utils.calc_months import calcular_meses


class Patente(AuditMixin, models.Model):
    """
    La clase Patente contiene el modelo de datos de la patente
    municipal y su relación con el establecimiento y contribuyente
    """
    id = models.AutoField(primary_key=True)
    numero_patente = models.IntegerField('Número de patente', blank=True, null=True)
    fecha = models.DateField('Fecha', blank=True, null=True)
    exonerada = models.BooleanField('Patente exonerada', blank=True, null=True, default=False)
    suspendida = models.BooleanField('Patente suspendida', blank=True, null=True, default=False)
    contribuyente = models.ForeignKey(Contribuyente, on_delete=models.CASCADE)
    establecimiento = models.ForeignKey(Establecimiento, on_delete=models.CASCADE)

    def __str__(self):
        """
        :return: El número de la patente como un string
        """
        return 'Patente Nº {} - {}'.format(self.id, self.establecimiento.nombre)

    def get_pago_esta_vencido(self):
        """
        :return: True or False en caso de que el pago esté vencido
        """
        hoy = date.today()
        vencimiento = self.get_vencimiento()
        if hoy > vencimiento:
            return True
        else:
            return False

    def get_estado(self):
        """
        :return: El estado actual de la patente: suspendidad, exonerada o sin estado
        """
        if self.suspendida:
            return '<span class="badge badge-danger">Suspendida</span>'
        elif self.exonerada:
            return '<span class="badge badge-success">Exonerada</span>'
        else:
            return '<span class="badge badge-light">-</span>'

    def to_json(self):
        """
        :return: Un diccionario de los atributos de la clase Patente
        """
        item = model_to_dict(self)
        item['ruc'] = self.contribuyente.ruc
        item['tipocontribuyente'] = self.contribuyente.tipocontribuyente.nombre
        item['nombre_establecimiento'] = self.establecimiento.nombre
        item['total_patrimonio'] = self.establecimiento.total_patrimonio
        item['nombre_contribuyente'] = self.contribuyente.get_nombre()
        item['estado'] = self.get_estado()
        item['estado_pago'] = self.get_pago_esta_vencido()
        item['dias_retraso'] = self.get_dias_retraso().days if self.get_pago_esta_vencido() else 0
        return item

    def get_impuesto(self):
        """
        :return: El total de impuesto de una clase patente
        """
        return calcular_impuesto(self.establecimiento.total_patrimonio)

    def get_ultimo_pago(self):
        """
        :return: La fecha del ultimo pago abonado de la patente
        """
        return fecha_ultimo_pago(self.id)

    def get_dias_retraso(self):
        f1 = self.get_vencimiento()
        today = date.today()
        return today - f1

    def get_anio_anterior(self):
        """
        :return: Primera vez en caso de ser apertura y el año anterior en caso
        de renovación
        """
        if self.get_ultimo_pago() == self.establecimiento.fecha_inicio_actividad:
            return 'Primera vez'
        else:
            return self.get_ultimo_pago().year

    def get_vencimiento(self):
        """
        :return: La fecha de vencimiento de cada patente en base al noveno dígito de cedula
        del contribuyente
        """
        ultimo_anio = self.get_ultimo_pago().year
        anio_actual = datetime.now().year
        try:
            if self.get_ultimo_pago() == self.establecimiento.fecha_inicio_actividad:
                return self.get_ultimo_pago() + timedelta(days=30)

            if ultimo_anio == anio_actual:
                fecha_vencimiento = self.contribuyente.get_fecha_vencimiento().replace(year=anio_actual + 1)
                return fecha_vencimiento
            else:
                fecha_vencimiento = self.contribuyente.get_fecha_vencimiento().replace(year=ultimo_anio + 1)
                return fecha_vencimiento
        except Exception as e:
            print(e)
        return date.today()

    def get_interes(self):
        """
        :return: El total del interes de la patente basado en el cálculo del impuesto
        """
        fecha_actual = date.today()
        fecha_vencimiento = self.get_vencimiento()

        if fecha_actual > fecha_vencimiento:
            meses_retraso = calcular_meses(fecha_vencimiento, fecha_actual)
            impuesto = float(self.get_impuesto())
            total = impuesto * meses_retraso * 0.03
            return format(total, '.2f')
        else:
            return format(0.00, '.2f')

    def get_multa(self):
        """
        :return: El total de la multa que debe pagar el contribuyente en caso de mora
        """
        fecha_vencimiento = self.get_vencimiento()
        fecha_actual = date.today()
        impuesto = float(self.get_impuesto())

        if fecha_actual > fecha_vencimiento:
            suma = 0.0
            multas = calc_meses_multa(fecha_vencimiento, fecha_actual)
            for i in multas:
                suma += impuesto * float(i.porcentaje)
            return format(suma, '.2f')
        else:
            return format(0.00, '.2f')

    def get_total_parcial(self):
        try:
            impuesto = 0.0 if self.exonerada > 0 else float(self.get_impuesto())
            interes = float(self.get_interes())
            multa = float(self.get_multa())
            total = impuesto + interes + multa
            return format(total, '.2f')
        except Exception as e:
            print(e)
        return 0.0

    class Meta:
        db_table = "patente"


class DetallePatente(AuditMixin, models.Model):
    """
    El modelo DetallePatente representa un historico de los
    movimientos de patente, en caso de apertura o renovación
    """
    id = models.AutoField(primary_key=True)
    fecha = models.DateField('Fecha de tramite', default=now, blank=True, null=True)
    impuesto = models.DecimalField(
        'Impuesto',
        decimal_places=2,
        default=0.00,
        max_digits=9,
        blank=True,
        null=True
    )
    interes = models.DecimalField(
        'Interes',
        decimal_places=2,
        default=0.00,
        max_digits=9,
        blank=True,
        null=True
    )
    multa = models.DecimalField(
        'Multa',
        decimal_places=2,
        default=0.00,
        max_digits=9,
        blank=True,
        null=True
    )
    servicios_administrativos = models.DecimalField(
        'Servicios administrativos',
        decimal_places=2,
        default=0.99,
        max_digits=9,
        blank=False,
        null=False
    )
    patente = models.ForeignKey(Patente, on_delete=models.CASCADE)

    def __str__(self):
        """
        :return: Una cadena de texto que contiene el id del detalle y el nombre del establecimiento
        asociado a la patente
        """
        return 'Detalle {} - Patente {}'.format(self.id, self.patente.establecimiento.nombre)

    def get_total(self):
        """
        :return: La sumatoria de los valores de impuesto, interes, multa y servicios administrativos
        """
        total = 0
        try:
            if self.impuesto or self.interes or self.multa or self.servicios_administrativos:
                total = self.impuesto + self.interes + self.multa + self.servicios_administrativos
        except Exception as e:
            print(e)
        return format(total, '.2f')

    def to_json(self):
        """
        :return: Un diccionario de los atributos de la clase DetallePatente
        """
        item = model_to_dict(self)
        item['total'] = self.get_total()
        return item

    class Meta:
        db_table = "detalle_patente"


def fecha_ultimo_pago(id_patente):
    """
    Función que calcula la fecha del último pago que ha realizado el contribuyente
    :param id_patente: Identificador del modelo Patente
    :return: La fecha del último registro encontrado en el DetallePatente
    """
    try:
        query = DetallePatente.objects.filter(patente__id=id_patente).count()
        if query == 0:
            return Patente.objects.get(id=id_patente).establecimiento.fecha_inicio_actividad
        else:
            fecha = DetallePatente.objects.filter(patente__id=id_patente).order_by('-fecha')[0]
            return fecha.fecha
    except IndexError:
        return date.today()
