from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse, JsonResponse
from apps.utils.ajax import AjaxCreate,AjaxUpdate, AjaxDelete
from .forms import EstablecimientoForm
from .models import Establecimiento


# Create your views here.
class ListaEstablecimiento(ListView):
    model = Establecimiento
    template_name = 'establecimiento/index.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, *kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Establecimiento.objects.filter(estado=True):
                    data.append(i.to_json())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
            # print(e)
        return JsonResponse(data, safe=False)


class CrearEstablecimiento(AjaxCreate, CreateView):
    model = Establecimiento
    template_name = 'establecimiento/crear_establecimiento.html'
    form_class = EstablecimientoForm
    success_url = reverse_lazy('establecimiento:lista_establecimiento')


class EditarEstablecimiento(AjaxUpdate, UpdateView):
    model = Establecimiento
    form_class = EstablecimientoForm
    template_name = 'establecimiento/editar_establecimiento.html'
    success_url = reverse_lazy('establecimiento:lista_establecimiento')


class EliminarEstablecimiento(AjaxDelete, DeleteView):
    model = Establecimiento
    template_name = 'establecimiento/eliminar.html'
    success_url = reverse_lazy('establecimiento:lista_establecimiento')
