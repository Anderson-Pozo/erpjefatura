import json
from django.core.serializers import serialize
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.http import HttpResponse, JsonResponse
from .models import Impuesto, Vencimiento, Multa
from .forms import MultaForm
from apps.utils.ajax import AjaxCreate, AjaxUpdate


# Create your views here.
class ListaVencimiento(ListView):
    model = Vencimiento
    template_name = 'impuesto/vencimiento/index.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, *kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Vencimiento.objects.all():
                    data.append(i.to_json())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)


class ListaMulta(ListView):
    model = Multa
    template_name = 'impuesto/multa/index.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, *kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Multa.objects.all():
                    data.append(i.to_json())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)


class CrearMulta(AjaxCreate, CreateView):
    model = Multa
    form_class = MultaForm
    template_name = 'impuesto/multa/crear_multa.html'
    success_url = reverse_lazy('impuesto:lista_multa')

    # def post(self, request, *args, **kwargs):
    #     if request.is_ajax():
    #         form = self.form_class(data=request.POST, files=request.FILES)
    #         if form.is_valid():
    #             form.save()
    #             mensaje = f'{self.model.__name__} registrado correctamente!'
    #             error = 'No hay error!'
    #             response = JsonResponse({'mensaje': mensaje, 'error': error})
    #             response.status_code = 201
    #             return response
    #         else:
    #             mensaje = f'{self.model.__name__} no se ha podido registrar!'
    #             # print(form.errors)
    #             error = form.errors
    #             response = JsonResponse({'mensaje': mensaje, 'error': error})
    #             response.status_code = 400
    #             return response
    #     return redirect('impuesto:lista_multa')


class EditarMulta(AjaxUpdate, UpdateView):
    model = Multa
    form_class = MultaForm
    template_name = 'impuesto/multa/editar_multa.html'
    success_url = reverse_lazy('impuesto:lista_multa')


class ListaImpuesto(ListView):
    model = Impuesto
    template_name = 'impuesto/impuesto/index.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, *kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Impuesto.objects.all():
                    data.append(i.to_json())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
