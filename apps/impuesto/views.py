from django.shortcuts import render
from django.views.generic import ListView
from .models import Impuesto, Vencimiento


# Create your views here.
class ListaVencimiento(ListView):
    model = Vencimiento
    template_name = 'impuesto/listado_vencimiento.html'
