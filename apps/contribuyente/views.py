from django.http import JsonResponse
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.utils.ajax import AjaxList, AjaxCreate, AjaxUpdate, AjaxDelete
from .forms import ContribuyenteNaturalForm, ContribuyenteJuridicoForm
from .models import Natural, Juridico, Contribuyente
from apps.usuario.mixins import AdminMixin


class ListaContribuyenteNatural(AdminMixin, AjaxList, ListView):
    model = Natural
    template_name = 'contribuyente/natural/index.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, *kwargs)


class CrearContribuyenteNatural(AdminMixin, AjaxCreate, CreateView):
    model = Natural
    form_class = ContribuyenteNaturalForm
    template_name = 'contribuyente/natural/crear_contribuyente.html'
    success_url = reverse_lazy('contribuyente:lista_contribuyente_natural')


class EditarContribuyenteNatural(AdminMixin, AjaxUpdate, UpdateView):
    model = Natural
    form_class = ContribuyenteNaturalForm
    template_name = 'contribuyente/natural/editar_contribuyente.html'
    success_url = reverse_lazy('contribuyente:lista_contribuyente_natural')


class EliminarContribuyenteNatural(AdminMixin, AjaxDelete, DeleteView):
    model = Natural
    template_name = 'contribuyente/natural/eliminar.html'
    success_url = reverse_lazy('contribuyente:lista_contribuyente_natural')


# Clases del contribuyente juridico
class ListaContribuyenteJuridico(AdminMixin, AjaxList, ListView):
    model = Juridico
    template_name = 'contribuyente/juridico/index.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, *kwargs)


class CrearContribuyenteJuridico(AdminMixin, AjaxCreate, CreateView):
    model = Juridico
    form_class = ContribuyenteJuridicoForm
    template_name = 'contribuyente/juridico/crear.html'
    success_url = reverse_lazy('contribuyente:lista_contribuyente_juridico')


class EditarContribuyenteJuridico(AdminMixin, AjaxUpdate, UpdateView):
    model = Juridico
    form_class = ContribuyenteJuridicoForm
    template_name = 'contribuyente/juridico/editar.html'
    success_url = reverse_lazy('contribuyente:lista_contribuyente_juridico')


class EliminarContribuyenteJuridico(AdminMixin, AjaxDelete, DeleteView):
    model = Juridico
    template_name = 'contribuyente/juridico/eliminar.html'
    success_url = reverse_lazy('contribuyente:lista_contribuyente_juridico')
