import json
from django.core.serializers import serialize
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.http import HttpResponse
from .models import Establecimiento


# Create your views here.
class IndexEstablecimiento(ListView):
    model = Establecimiento
    template_name = 'establecimiento/index.html'

    # def get(self, request, *args, **kwargs):
    #     if request.is_ajax():
    #         return HttpResponse(serialize('json', self.get_queryset()), 'application/json')
    #     else:
    #         return redirect('index')
