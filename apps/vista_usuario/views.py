from datetime import date
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView
from django.http import HttpResponse, JsonResponse
from apps.patente.models import Patente, DetallePatente
from apps.establecimiento.models import Establecimiento


class Index(LoginRequiredMixin, TemplateView):
    template_name = 'consulta/index.html'

    # user = request.user.username

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, *kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            user = request.user.username
            action = request.POST['action']
            if action == 'search_data':
                data = []
                for i in Patente.objects.filter(contribuyente__ruc=user):
                    data.append(i.to_json())
            elif action == 'search_establ':
                data = []
                for i in Establecimiento.objects.filter(patente__contribuyente__ruc=user):
                    data.append(i.to_json())
            elif action == 'search_details':
                data = []
                for i in DetallePatente.objects.filter(patente__id=request.POST['id']):
                    data.append(i.to_json())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fechas'] = DetallePatente.objects.filter(
            patente__contribuyente__ruc=self.request.user.username).order_by('-fecha')[0:3]
        # print(context)
        return context


class Calendario(LoginRequiredMixin, TemplateView):
    template_name = 'consulta/calendario.html'

    def get_context_data(self, **kwargs):
        patentes = Patente.objects.filter(contribuyente__ruc=self.request.user.username)
        context = super().get_context_data(**kwargs)
        context['fechas'] = DetallePatente.objects.filter(patente__contribuyente__ruc=self.request.user.username)
        context['vencimiento'] = date(2021, 2, 27)
        context['hoy'] = date.today()
        context['patentes'] = patentes
        return context


class Informacion(LoginRequiredMixin, TemplateView):
    template_name = 'consulta/informacion.html'
