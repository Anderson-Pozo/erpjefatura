from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, TemplateView
from django.http import HttpResponse, JsonResponse
from .models import Patente, DetallePatente
from .forms import PatenteForm
from apps.utils.ajax import AjaxCreate, AjaxUpdate, AjaxDelete


class ListaCatastro(ListView):
    model = Patente
    template_name = 'patente/catastro/index.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, *kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Patente.objects.all():
                    data.append(i.to_json())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)


class CrearContribuyente(TemplateView):
    template_name = 'patente/apertura/paso1.html'
