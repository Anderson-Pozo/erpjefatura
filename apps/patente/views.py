from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView, View, UpdateView, DeleteView
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from apps.contribuyente.models import Natural, Juridico
from apps.contribuyente.forms import ContribuyenteNaturalForm as NaturalForm, ContribuyenteJuridicoForm as JuridicoForm
from apps.establecimiento.forms import EstablecimientoForm
from apps.administrador.mails import send_mail_thread
from .models import Patente, DetallePatente
from apps.establecimiento.models import Establecimiento
from apps.utils.ajax import AjaxList, AjaxUpdate
from apps.usuario.mixins import AdminMixin
from .forms import *

from django.template.loader import get_template
from xhtml2pdf import pisa


class ListaCatastro(AdminMixin, ListView):
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


class SuspenderPatente(AdminMixin, DeleteView):
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


class ExonerarPatente(AdminMixin, DeleteView):
    model = Patente
    template_name = 'patente/catastro/exonerar.html'
    success_url = reverse_lazy('patente:lista_catastro')

    def delete(self, request, *args, **kwargs):
        if request.is_ajax():
            modelo = self.get_object()
            if modelo.exonerada:
                modelo.exonerada = False
            else:
                modelo.exonerada = True
            modelo.save()
            message = f'{self.model.__name__} fue exonerada'
            error = 'No hay error'
            response = JsonResponse({'message': message, 'error': error})
            response.status_code = 201
            return response
        else:
            return self.success_url


class EnviarCorreo(AdminMixin, TemplateView):
    template_name = 'patente/catastro/enviar_correo.html'
    success_url = reverse_lazy('patente:lista_catastro')

    def get_context_data(self, **kwargs):
        context = {
            'patente': Patente.objects.get(id=self.kwargs['pk'])
        }
        return context

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            try:
                email_destino = request.POST.get('email')
                patente_id = request.POST.get('id_patente')

                if email_destino and patente_id:
                    data = {'patente': Patente.objects.get(id=patente_id)}
                    send_mail_thread(email_destino, 2, data)
                    print('Correo enviado')
                    message = ' Correo enviado correctamente'
                    error = 'No hay error'
                    response = JsonResponse({'message': message, 'error': error})
                    response.status_code = 201
                    return response
                else:
                    message = f'Algo salió mal, no se pudo enviar el correo'
                    error = 'Error al procesar envio'
                    response = JsonResponse({'message': message, 'error': error})
                    response.status_code = 400
                    return response
            except Exception as e:
                print(e)
        else:
            return self.success_url


# Proceso de apertura de patente
class CrearNatural(AdminMixin, CreateView):
    """Vista de creación de un contribuyente natural."""
    model = Natural
    form_class = NaturalForm
    template_name = 'patente/apertura/crear_natural.html'
    success_url = reverse_lazy('patente:crear_establecimiento')


class CrearJuridico(AdminMixin, CreateView):
    """Vista de creación de un contribuyente juridico."""
    model = Juridico
    form_class = JuridicoForm
    template_name = 'patente/apertura/crear_juridico.html'
    success_url = reverse_lazy('patente:crear_establecimiento')


class CrearEstablecimiento(AdminMixin, CreateView):
    """Vista de creación de un establecimiento."""
    model = Establecimiento
    form_class = EstablecimientoForm
    template_name = 'patente/apertura/crear_establecimiento.html'
    success_url = reverse_lazy('patente:crear_patente')


class CrearPatente(AdminMixin, CreateView):
    """Vista de creación de una patente."""
    model = Patente
    form_class = PatenteForm
    template_name = 'patente/apertura/crear_patente.html'
    success_url = reverse_lazy('patente:revision_declaracion')


class RevisionDeclaracion(AdminMixin, TemplateView):
    """TemplateView que muestra los datos asociados a la última patente creada"""
    template_name = "patente/apertura/revision_declaracion.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patente'] = Patente.objects.last()
        return context


class CreacionEspecie(AdminMixin, CreateView):
    """Vista de creación de un DetallePatente"""
    template_name = 'patente/apertura/crear_especie.html'
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


class RevisionEspecie(AdminMixin, TemplateView):
    """TemplateView que muestra los datos del ultimo Detalle de Patente creado"""
    template_name = "patente/apertura/revision_especie.html"

    def get_context_data(self, **kwargs):
        """
        :return: Diccionario con los datos del último registro de DetallePatente
        """
        context = super().get_context_data(**kwargs)
        context['detalle'] = DetallePatente.objects.last()
        return context


# Proceso de renovación de patente
class EspecieRenovacion(AdminMixin, CreateView):
    """Vista de revisión de DetallePatente una vez actualizada"""
    template_name = 'patente/renovacion/renovar_especie.html'
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
    template_name = "patente/renovacion/revision_especie.html"


# Vista de reportes
class ReportDeclaracion(AdminMixin, View):
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


class ReportEspecie(AdminMixin, View):
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

