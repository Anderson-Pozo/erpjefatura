from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from .models import Impuesto, Vencimiento, Multa
from .forms import MultaForm, ImpuestoForm, VencimientoForm
from apps.utils.ajax import AjaxList, AjaxCreate, AjaxUpdate


class ListaVencimiento(AjaxList, ListView):
    model = Vencimiento
    template_name = 'impuesto/vencimiento/index.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, *kwargs)


class EditarVencimiento(AjaxUpdate, UpdateView):
    model = Vencimiento
    form_class = VencimientoForm
    template_name = 'impuesto/vencimiento/editar_vencimiento.html'
    success_url = reverse_lazy('impuesto:lista_vencimiento')


# Clases Multa
class ListaMulta(AjaxList, ListView):
    model = Multa
    template_name = 'impuesto/multa/index.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, *kwargs)


class CrearMulta(AjaxCreate, CreateView):
    model = Multa
    form_class = MultaForm
    template_name = 'impuesto/multa/crear_multa.html'
    success_url = reverse_lazy('impuesto:lista_multa')


class EditarMulta(AjaxUpdate, UpdateView):
    model = Multa
    form_class = MultaForm
    template_name = 'impuesto/multa/editar_multa.html'
    success_url = reverse_lazy('impuesto:lista_multa')


# Clases impuesto
class ListaImpuesto(AjaxList, ListView):
    model = Impuesto
    template_name = 'impuesto/impuesto/index.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, *kwargs)


class EditarImpuesto(AjaxUpdate, UpdateView):
    model = Impuesto
    form_class = ImpuestoForm
    template_name = 'impuesto/impuesto/editar_impuesto.html'
    success_url = reverse_lazy('impuesto:lista_impuesto')
