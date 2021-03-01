from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView, View
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from apps.utils.ajax import AjaxList, AjaxCreate, AjaxUpdate, AjaxDelete
from .forms import PlusvaliaForm
from .models import Plusvalia, Alcabala
from django.shortcuts import render


from django.template.loader import get_template
from xhtml2pdf import pisa


class ListaPlusvalia(AjaxList, ListView):
    model = Plusvalia
    template_name = 'alcabala-plusvalia/index-plusvalia.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, *kwargs)


class CrearPlusvalia(CreateView):
    model = Plusvalia
    form_class = PlusvaliaForm
    template_name = 'alcabala-plusvalia/registro/paso2_plusvalia.html'
    success_url = reverse_lazy('alcabala:revision_alcabala')

    def get_context_data(self, **kwargs):
        context = {
            'alcabala': Alcabala.objects.last(),
            'form': self.form_class,
        }
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())


class RevisionPlusvalia(TemplateView):
    template_name = "alcabala-plusvalia/registro/paso4_revision2.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plusvalia'] = Plusvalia.objects.last()
        return context


class ReportPlusvalia(View):
    def get(self, request, *args, **kwargs):
        try:
            template = get_template('alcabala-plusvalia/reportes/report_plusvalia.html')
            context = {
                'plusvalia': Plusvalia.objects.get(pk=self.kwargs['pk'])
            }
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            pisa_status = pisa.CreatePDF(
                html, dest=response)
            return response
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('plusvalia:lista_plusvalia'))
