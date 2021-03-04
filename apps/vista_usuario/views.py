from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, TemplateView
from django.http import HttpResponse, JsonResponse
from apps.utils.ajax import AjaxList, AjaxCreate, AjaxUpdate, AjaxDelete


class Index(AjaxList, TemplateView):
    # model = VistaUsuario
    template_name = 'vista_usuario/index.html'

