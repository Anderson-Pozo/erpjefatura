from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic import TemplateView
from apps.patente.models import DetallePatente
from apps.usuario.models import Logs, User


# Create your views here.
class Index(TemplateView):
    template_name = 'administrador/index.html'

    @method_decorator(csrf_protect)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_superuser is False:
            return HttpResponseRedirect(reverse_lazy('vista_usuario:index_contribuyente'))
        else:
            return super(Index, self).dispatch(request, *args, **kwargs)

    @staticmethod
    def get_total_impuestos():
        total = 0.0
        for i in DetallePatente.objects.all():
            total += float(i.get_total())
        return total

    @staticmethod
    def get_last_logs():
        try:
            return Logs.objects.all().order_by('-action_time')[0:8]
        except:
            pass
        return []

    @staticmethod
    def get_last_users():
        return User.objects.all().order_by('last_login')[0:6]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total'] = self.get_total_impuestos()
        context['logs'] = self.get_last_logs()
        context['users'] = self.get_last_users()
        # print(context)
        return context
