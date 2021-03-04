from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView, View
from django.http import HttpResponse, JsonResponse
from apps.utils.ajax import AjaxList, AjaxCreate, AjaxUpdate, AjaxDelete
# from .forms import EstablecimientoForm
from .models import VistaUsuario


class Index(AjaxList, ListView):
    model = VistaUsuario
    template_name = 'vista_usuario/index.html'


@method_decorator(csrf_exempt)
def dispatch(self, request, *args, **kwargs):
    return super().dispatch(request, *args, *kwargs)

class Help(TemplateView):
    model = VistaUsuario
    template_name = 'vista_usuario/help.html'