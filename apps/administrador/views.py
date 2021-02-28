from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from apps.patente.models import DetallePatente
from apps.usuario.models import Logs, User


# Create your views here.
class Index(TemplateView):
    template_name = 'administrador/index.html'

    @staticmethod
    def get_total_impuestos():
        total = 0.0
        for i in DetallePatente.objects.all():
            total += float(i.get_total())
        return total

    @staticmethod
    def get_last_logs():
        data = []
        for i in Logs.objects.all().order_by('-action_time')[0:7]:
            data.append(i)
        return data

    @staticmethod
    def get_last_users():
        return User.objects.all().order_by('last_login')[0:6]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total'] = self.get_total_impuestos()
        context['logs'] = self.get_last_logs()
        context['users'] = self.get_last_users()
        print(context)
        return context
