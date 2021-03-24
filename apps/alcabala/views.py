from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView, View
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from apps.utils.ajax import *
from .forms import AlcabalaForm
from .models import Alcabala, Persona, Predio

from django.template.loader import get_template
from xhtml2pdf import pisa


class ListaAlcabala(AjaxList, ListView):
    model = Alcabala
    template_name = 'alcabala-plusvalia/index-alcabala.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, *kwargs)


class CrearAlcabala(CreateView):
    model = Alcabala
    form_class = AlcabalaForm
    template_name = 'alcabala-plusvalia/registro/paso1_alcabala.html'
    success_url = reverse_lazy('plusvalia:crear_plusvalia')


class RevisionAlcabala(TemplateView):
    template_name = "alcabala-plusvalia/registro/paso3_revision1.html"
    form_class = AlcabalaForm
    success_url = reverse_lazy('plusvalia:revision_plusvalia')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['alcabala'] = Alcabala.objects.last()
        return context


class ReportAlcabala(View):
    def get(self, request, *args, **kwargs):
        try:
            template = get_template('alcabala-plusvalia/reportes/report_alcabala.html')
            context = {
                'alcabala': Alcabala.objects.get(pk=self.kwargs['pk'])
            }
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            pisa_status = pisa.CreatePDF(
                html, dest=response)
            return response
        except Exception as e:
            print(e)
        return HttpResponseRedirect(reverse_lazy('plusvalia:revision_plusvalia'))


class GetPersonas(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs, ):
        data = {}
        try:
            action = request.POST['action']
            if action == 'autoselect':
                data = []
                for i in Persona.objects.filter(numero_cedula__icontains=request.POST['term'])[0:5]:
                    item = i.to_json()
                    item['text'] = i.nombres + ' ' + i.apellidos
                    data.append(item)
            elif action == 'getpredio':
                data = []
                for i in Predio.objects.filter(clave_catastral__icontains=request.POST['term'])[0:5]:
                    item = i.to_json()
                    item['text'] = i.clave_catastral
                    data.append(item)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

