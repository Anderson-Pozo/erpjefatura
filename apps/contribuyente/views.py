import json
from django.core.serializers import serialize
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.http import HttpResponse, JsonResponse
from .models import Contribuyente
from .forms import ContribuyenteForm


# Create your views here.
class ListaContribuyente(ListView):
    model = Contribuyente
    template_name = 'contribuyente/index.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, *kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Contribuyente.objects.all():
                    # data['tipocontribuyente'] = i.tipocontribuyente.nombre
                    data.append(i.to_json())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    # def get(self, request, *args, **kwargs):
    #     if request.is_ajax():
    #         return HttpResponse(serialize('json', self.get_queryset()), 'application/json')
    #     else:
    #         return redirect('contribuyente:home')


class CrearContribuyente(CreateView):
    model = Contribuyente
    form_class = ContribuyenteForm
    template_name = 'contribuyente/crear_contribuyente.html'
    # success_url = reverse_lazy('contribuyente:lista_contribuyentes')

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(data=request.POST, files=request.FILES)
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} registrado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido registrar!'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        return redirect('contribuyente:lista_contribuyentes')
