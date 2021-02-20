from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse, JsonResponse
from apps.utils.ajax import AjaxList, AjaxCreate, AjaxUpdate, AjaxDelete
from .forms import PlusvaliaForm
from .models import Plusvalia


class ListaPlusvalia(AjaxList, ListView):
    model = Plusvalia
    template_name = 'plusvalia/index.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, *kwargs)


class CrearPlusvalia(CreateView):
    model = Plusvalia
    form_class =  PlusvaliaForm
    template_name = 'alcabala-plusvalia/registro/paso2_plusvalia.html'
    success_url = reverse_lazy('establecimiento:lista_establecimiento')