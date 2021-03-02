from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView, View, UpdateView
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from apps.contribuyente.models import Natural, Juridico, Contribuyente
from apps.establecimiento.models import Establecimiento
from apps.contribuyente.forms import ContribuyenteNaturalForm as NaturalForm, ContribuyenteJuridicoForm as JuridicoForm
from apps.establecimiento.forms import EstablecimientoForm
from apps.utils.ajax import AjaxList
from .models import Patente, DetallePatente
from .forms import PatenteForm, DetalleForm

from django.template.loader import get_template
from xhtml2pdf import pisa


class ListaCatastro(AjaxList, ListView):
    model = Patente
    template_name = 'patente/catastro/index.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, *kwargs)


class CrearContribuyente(TemplateView):
    template_name = 'patente/apertura/paso1_contribuyente.html'

    def get(self, request, *args, **kwargs):
        form_natural = NaturalForm(self.request.GET or None, prefix="natural")
        form_juridico = JuridicoForm(self.request.GET or None, prefix="juridico")
        context = super(CrearContribuyente, self).get_context_data(**kwargs)
        context['form_natural'] = form_natural
        context['form_juridico'] = form_juridico
        return self.render_to_response(context)


class CrearNatural(CreateView):
    model = Natural
    form_class = NaturalForm
    template_name = 'patente/apertura/paso1_contribuyente_natural.html'
    success_url = reverse_lazy('patente:crear_establecimiento')


class CrearJuridico(CreateView):
    model = Juridico
    form_class = JuridicoForm
    template_name = 'patente/apertura/paso1_contribuyente_juridico.html'
    success_url = reverse_lazy('patente:crear_establecimiento')


class CrearEstablecimiento(CreateView):
    model = Establecimiento
    form_class = EstablecimientoForm
    template_name = 'patente/apertura/paso2_establecimiento.html'
    success_url = reverse_lazy('patente:crear_patente')


class CrearPatente(CreateView):
    model = Patente
    form_class = PatenteForm
    template_name = 'patente/apertura/paso3_patente.html'
    success_url = reverse_lazy('patente:revision_declaracion')


class RevisionDeclaracion(TemplateView):
    template_name = "patente/apertura/paso3_revision_declaracion.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patente'] = Patente.objects.last()
        return context


class ReportDeclaracion(View):
    def get(self, request, *args, **kwargs):
        try:
            template = get_template('patente/reportes/declaracion_report.html')
            context = {
                'patente': Patente.objects.get(pk=self.kwargs['pk'])
            }
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            pisa_status = pisa.CreatePDF(
                html, dest=response)
            return response
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('patente:lista_catastro'))


class CreacionEspecie(CreateView):
    template_name = 'patente/apertura/paso4_especie.html'
    form_class = DetalleForm
    success_url = reverse_lazy('patente:revision_especie')

    def get_context_data(self, **kwargs):
        context = {
            'patente': Patente.objects.last(),
            'form': self.form_class,
        }
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())


class RevisionEspecie(TemplateView):
    template_name = "patente/apertura/paso4_revision_especie.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['detalle'] = DetallePatente.objects.last()
        return context


class ReportEspecie(View):
    def get(self, request, *args, **kwargs):
        try:
            template = get_template('patente/reportes/especie_report.html')
            context = {
                'detalle': DetallePatente.objects.get(pk=self.kwargs['pk'])
            }
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            pisa_status = pisa.CreatePDF(
                html, dest=response)
            return response
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('patente:lista_catastro'))


class ActualizarDeclaracion(UpdateView):
    model = Patente
    form_class = PatenteForm
    template_name = 'patente/actualizar/paso1_actualizar_declaracion.html'
    success_url = reverse_lazy('patente:revision_declaracion')
