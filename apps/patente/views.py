from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, TemplateView, CreateView
from django.http import HttpResponse, JsonResponse
from .models import Patente, DetallePatente
from apps.contribuyente.models import Natural, Juridico, Contribuyente
from apps.establecimiento.models import Establecimiento
from .forms import PatenteForm
from apps.utils.ajax import AjaxCreate, AjaxUpdate, AjaxDelete
from apps.contribuyente.forms import ContribuyenteNaturalForm, ContribuyenteJuridicoForm
from apps.establecimiento.forms import EstablecimientoForm


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


# class CrearContribuyenteNatural(TemplateView):
#     template_name = 'patente/apertura/paso1_contribuyente.html'


class CrearContribuyente(AjaxCreate, CreateView):
    # model = Contribuyente
    model = Natural
    # model = Juridico
    form_class = ContribuyenteNaturalForm
    # form_class = ContribuyenteJuridicoForm
    template_name = 'patente/apertura/paso1_contribuyente.html'
    # success_url = reverse_lazy('patente:crear_contribuyente_natural')

class CrearContribuyenteJuridico(AjaxCreate, CreateView):
    model = Contribuyente
    model = Natural
    model = Juridico
    form_class = ContribuyenteNaturalForm
    form_class = ContribuyenteJuridicoForm
    template_name = 'patente/apertura/paso1_contribuyente.html'
    # success_url = reverse_lazy('patente:crear_contribuyente_natural')

class CrearEstablecimiento(AjaxCreate, CreateView):
    model = Establecimiento
    form_class = EstablecimientoForm
    template_name = 'patente/apertura/paso2_establecimiento.html'
    # success_url = reverse_lazy('patente:crear_contribuyente_natural')


class CrearPatente(AjaxCreate, CreateView):
    model = Patente
    form_class = PatenteForm
    template_name = 'patente/apertura/paso3_detalle.html'
    # success_url = reverse_lazy('patente:crear_contribuyente_natural')
