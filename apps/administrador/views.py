from datetime import datetime, date
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic import TemplateView
from apps.patente.models import DetallePatente, Patente
from apps.alcabala.models import Alcabala
from apps.plusvalia.models import Plusvalia
from apps.usuario.models import Logs, User
from django.conf import settings

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.template.loader import render_to_string
from django.conf import settings


# Create your views here.
class Index(TemplateView):
    template_name = 'administrador/index.html'
    year = datetime.now().year
    month = datetime.now().month

    @method_decorator(csrf_protect)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_superuser is False:
            return HttpResponseRedirect(reverse_lazy('vista_usuario:index_contribuyente'))
        else:
            return super(Index, self).dispatch(request, *args, **kwargs)

    def get_total_impuestos(self):
        total = 0.0
        for i in DetallePatente.objects.filter(fecha__year=self.year):
            total += float(i.get_total())
        return format(total, '.2f')

    def get_total_alcabalas(self):
        total = 0.0
        try:
            for i in Alcabala.objects.filter(fecha__year=self.year):
                total += float(i.get_total())
        except Exception as error:
            print(error)
        return format(total, '.2f')

    def get_total_plusvalias(self):
        total = 0.0
        try:
            for i in Plusvalia.objects.filter(fecha_tramite__year=self.year):
                total += float(i.get_total())
        except Exception as error:
            print(error)
        return format(total, '.2f')

    @staticmethod
    def get_last_logs():
        try:
            return Logs.objects.all().order_by('-action_time')[0:8]
        except Exception as error:
            print(error)
        return []

    @staticmethod
    def get_last_users():
        try:
            return User.objects.all().order_by('-last_login')[0:6]
        except Exception as error:
            print(error)
        return []

    @staticmethod
    def get_valores_patente_by_year(year):
        data = []
        total = 0
        try:
            for m in range(1, 13):
                for i in DetallePatente.objects.filter(fecha__year=year, fecha__month=m):
                    total += float(i.get_total())
                data.append(total)
                total = 0
        except Exception as error:
            print(error)
        return data

    # @staticmethod
    # def get_patentes_pendientes():
    #     data = []
    #     current_date = date.today()
    #     for patente in Patente.objects.all():
    #         if current_date > patente.get_vencimiento():
    #             data.append(patente)
    #     return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_patentes'] = self.get_total_impuestos()
        context['total_alcabalas'] = self.get_total_alcabalas()
        context['total_plusvalias'] = self.get_total_plusvalias()
        context['logs'] = self.get_last_logs()
        context['users'] = self.get_last_users()
        context['get_values_graph_current_year'] = self.get_valores_patente_by_year(self.year)
        context['get_values_previous_year'] = self.get_valores_patente_by_year(self.year - 1)
        context['get_previous_year'] = self.year - 1
        # context['get_pagos_pendientes'] = self.get_patentes_pendientes()
        return context


def send_mail_contri(request):
    try:
        mailServer = smtplib.SMTP(settings.EMAIL_HOST, 587)
        print(mailServer.ehlo())
        mailServer.starttls()
        print(mailServer.ehlo())
        print(mailServer.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD))
        print('Conectado..')

        message = MIMEMultipart()
        message['From'] = settings.EMAIL_HOST_USER
        message['To'] = 'anderam92@gmail.com'
        message['Subject'] = 'Notificación de pago GAD Municipal Huaca'

        context = render_to_string('administrador/email_temp/noti_pago.html',
                                   {'user': User.objects.get(username='0401798475')}
                                   )
        message.attach(MIMEText(context, 'html'))

        mailServer.sendmail(
            settings.EMAIL_HOST_USER,
            'anderam92@gmail.com',
            message.as_string()
        )

        print('Correo enviado correctamente')
        return redirect('index')
    except Exception as error:
        print(error)
