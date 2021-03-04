from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.http import HttpResponse, JsonResponse
from apps.utils.ajax import AjaxList

# Create your views here.


class Index(TemplateView):
    # model = VistaUsuario
    template_name = 'vista_usuario/index.html'



