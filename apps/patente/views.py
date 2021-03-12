from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView, View, UpdateView, DeleteView
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from apps.contribuyente.models import *
from apps.establecimiento.models import Establecimiento
from apps.contribuyente.forms import ContribuyenteNaturalForm as NaturalForm, ContribuyenteJuridicoForm as JuridicoForm
from apps.establecimiento.forms import EstablecimientoForm
from apps.utils.ajax import AjaxList, AjaxUpdate
from .models import Patente, DetallePatente
from .forms import *

from django.template.loader import get_template
from xhtml2pdf import pisa


class ListaCatastro(ListView):
    """ListView que genera un listado de registros de Patente"""
    model = Patente
    template_name = 'patente/catastro/index.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, *kwargs)

    def post(self, request, *args, **kwargs):
        """ Método que se ejecuta cuando se realiza una petición POST

        :param request: Petición que realiza el cliente
        :param args: Lista de argumentos posicionales
        :param kwargs: Diccionario de parámetros y argumentos
        :return: Un objeto Json con los registros de Patente y DetallePatente
        """
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in self.model.objects.all():
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


class SuspenderPatente(DeleteView):
    model = Patente
    template_name = 'patente/catastro/suspender.html'
    success_url = reverse_lazy('patente:lista_catastro')

    def delete(self, request, *args, **kwargs):
        if request.is_ajax():
            modelo = self.get_object()
            if modelo.suspendida:
                modelo.suspendida = False
            else:
                modelo.suspendida = True
            modelo.save()
            message = f'{self.model.__name__} fue suspendida'
            error = 'No hay error'
            response = JsonResponse({'message': message, 'error': error})
            response.status_code = 201
            return response
        else:
            return self.success_url


class EditarPatente(AjaxUpdate, UpdateView):
    model = Patente
    form_class = PatenteForm
    template_name = 'patente/catastro/editar.html'
    success_url = reverse_lazy('patente:lista_catastro')


# Proceso de apertura de patente
class CrearNatural(CreateView):
    """Vista de creación de un contribuyente natural."""
    model = Natural
    form_class = NaturalForm
    template_name = 'patente/apertura/paso1_contribuyente_natural.html'
    success_url = reverse_lazy('patente:crear_establecimiento')


class CrearJuridico(CreateView):
    """Vista de creación de un contribuyente juridico."""
    model = Juridico
    form_class = JuridicoForm
    template_name = 'patente/apertura/paso1_contribuyente_juridico.html'
    success_url = reverse_lazy('patente:crear_establecimiento')


class CrearEstablecimiento(CreateView):
    """Vista de creación de un establecimiento."""
    model = Establecimiento
    form_class = EstablecimientoForm
    template_name = 'patente/apertura/paso2_establecimiento.html'
    success_url = reverse_lazy('patente:crear_patente')


class CrearPatente(CreateView):
    """Vista de creación de una patente."""
    model = Patente
    form_class = PatenteForm
    template_name = 'patente/apertura/paso3_patente.html'
    success_url = reverse_lazy('patente:revision_declaracion')


class RevisionDeclaracion(TemplateView):
    """TemplateView que muestra los datos asociados a la última patente creada"""
    template_name = "patente/apertura/paso3_revision_declaracion.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patente'] = Patente.objects.last()
        return context


class CreacionEspecie(CreateView):
    """Vista de creación de un DetallePatente"""
    template_name = 'patente/apertura/paso4_especie.html'
    form_class = DetalleForm
    success_url = reverse_lazy('patente:revision_especie')

    def get_context_data(self, **kwargs):
        """Método que retorna los datos de la última patente hacia el template"""
        context = {
            'patente': Patente.objects.last(),
            'form': self.form_class,
        }
        return context

    def get(self, request, *args, **kwargs):
        """Se ejecuta en una petición GET renderizando el template y el contexto"""
        return render(request, self.template_name, self.get_context_data())


class RevisionEspecie(TemplateView):
    """TemplateView que muestra los datos del ultimo Detalle de Patente creado"""
    template_name = "patente/apertura/paso4_revision_especie.html"

    def get_context_data(self, **kwargs):
        """
        :return: Diccionario con los datos del último registro de DetallePatente
        """
        context = super().get_context_data(**kwargs)
        context['detalle'] = DetallePatente.objects.last()
        return context


# Vista de reportes
class ReportDeclaracion(View):
    """Vista que genera un reporte PDF del formulario de declaración de patente"""
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
        except Exception as error:
            print(error)
        return HttpResponseRedirect(reverse_lazy('patente:lista_catastro'))


class ReportEspecie(View):
    """Vista que genera un reporte PDF de la especie de Patente Municipal"""
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
        except Exception as error:
            print(error)
        return HttpResponseRedirect(reverse_lazy('patente:lista_catastro'))


# Proceso de modificación
class ActualizarDeclaracion(UpdateView):
    """UpdateView que actualiza los datos de la clase Patente"""
    model = Patente
    form_class = PatenteForm
    template_name = 'patente/actualizar/1_actualizar_declaracion.html'
    success_url = reverse_lazy('patente:revision_declaracion')


class RevisionModificada(RevisionDeclaracion):
    """Vista de revisión de Patente una vez actualizada"""
    template_name = "patente/actualizar/2_revision_declaracion.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patente'] = Patente.objects.get(pk=self.kwargs['pk'])
        return context


class EspecieRenovacion(CreateView):
    """Vista de revisión de DetallePatente una vez actualizada"""
    template_name = 'patente/actualizar/3_especie_renovada.html'
    form_class = DetalleForm
    success_url = reverse_lazy('patente:rev_especie')

    def get_context_data(self, **kwargs):
        context = {
            'patente': Patente.objects.get(pk=self.kwargs['pk']),
            'form': self.form_class,
        }
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())


class RevisionEspModificada(RevisionEspecie):
    """Vista para revisión de datos de Especie Patente luego de ser actualizada"""
    template_name = "patente/actualizar/4_rev_especie_modificada.html"
