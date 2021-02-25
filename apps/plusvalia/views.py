from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse, JsonResponse
from apps.utils.ajax import AjaxList, AjaxCreate, AjaxUpdate, AjaxDelete
from .forms import PlusvaliaForm
from .models import Plusvalia, Alcabala
from django.shortcuts import render


class ListaPlusvalia(AjaxList, ListView):
    model = Plusvalia
    template_name = 'alcabala-plusvalia/index-plusvalia.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, *kwargs)


class CrearPlusvalia(CreateView):
    model = Plusvalia
    form_class =  PlusvaliaForm
    template_name = 'alcabala-plusvalia/registro/paso2_plusvalia.html'
    success_url = reverse_lazy('plusvalia:lista_plusvalia')

    def get_context_data(self, **kwargs):
        context = {
            'alcabala' : Alcabala.objects.last(),
            'form' : self.form_class,
        }
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())