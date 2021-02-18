from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse, JsonResponse
from apps.utils.ajax import AjaxList, AjaxCreate, AjaxUpdate, AjaxDelete
from .forms import AlcabalaForm
from .models import Alcabala


class CrearAlcabala(CreateView):
    model = Alcabala
    form_class =  AlcabalaForm
    template_name = 'alcabala/crear_alcabala.html'
    success_url = reverse_lazy('establecimiento:lista_establecimiento')

    # @method_decorator(csrf_exempt)
    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(request, *args, *kwargs)

# class CrearAlcabala(AjaxCreate, CreateView):
#     model = Alcabala
#     template_name = 'alcabala/crear_alcabala.html'
#     form_class = AlcabalaForm
#     # success_url = reverse_lazy('establecimiento:lista_establecimiento')
#
#     @method_decorator(csrf_exempt)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, *kwargs)