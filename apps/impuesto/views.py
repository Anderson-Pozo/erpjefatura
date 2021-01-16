from django.shortcuts import render
from django.views.generic import ListView
from .models import Impuesto, Vencimiento, Multa
from django.utils.decorators import method_decorator
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
class ListaVencimiento(ListView):
    model = Vencimiento
    template_name = 'impuesto/vencimiento/index.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, *kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Vencimiento.objects.all():
                    data.append(i.to_json())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

class ListaMulta(ListView):
    model = Multa
    template_name = 'impuesto/multa/index.html'


class ListaImpuesto(ListView):
    model = Impuesto
    template_name = 'impuesto/impuesto/index.html'
