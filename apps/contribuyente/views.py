import json
from django.core.serializers import serialize
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, TemplateView
from django.http import HttpResponse, JsonResponse
from .models import Contribuyente


# Create your views here.
class ListaContribuyente(ListView):
    model = Contribuyente
    template_name = 'contribuyente/index.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, *kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Contribuyente.objects.all():
                    # data['tipocontribuyente'] = i.tipocontribuyente.nombre
                    data.append(i.to_json())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    # def get(self, request, *args, **kwargs):
    #     if request.is_ajax():
    #         return HttpResponse(serialize('json', self.get_queryset()), 'application/json')
    #     else:
    #         return redirect('contribuyente:home')


class CrearContribuyente(TemplateView):
    model = Contribuyente
    template_name = 'contribuyente/crear_contribuyente.html'

