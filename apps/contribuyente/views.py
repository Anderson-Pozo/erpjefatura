import json
from django.core.serializers import serialize
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.http import HttpResponse
from .models import Contribuyente


# Create your views here.
class IndexContribuyente(ListView):
    model = Contribuyente
    template_name = 'contribuyente/index.html'

    # def get(self, request, *args, **kwargs):
    #     if request.is_ajax():
    #         return HttpResponse(serialize('json', self.get_queryset()), 'application/json')
    #     else:
    #         return redirect('index')
