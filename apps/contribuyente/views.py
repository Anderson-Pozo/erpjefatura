from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView
from django.http import JsonResponse
from .models import Natural, Juridico
from .forms import ContribuyenteNaturalForm, ContribuyenteJuridicoForm
from apps.utils.ajax import AjaxCreate


# Create your views here.
class ListaContribuyenteNatural(ListView):
    model = Natural
    template_name = 'contribuyente/natural/index.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, *kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in self.model.objects.filter(estado=True):
                    data.append(i.to_json())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)


class CrearContribuyenteNatural(AjaxCreate, CreateView):
    model = Natural
    form_class = ContribuyenteNaturalForm
    template_name = 'contribuyente/natural/crear_contribuyente.html'
    success_url = reverse_lazy('contribuyente:lista_contribuyente_natural')


class ListaContribuyenteJuridico(ListView):
    model = Juridico
    template_name = 'contribuyente/juridico/index.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, *kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Juridico.objects.filter(estado=True):
                    data.append(i.to_json())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)


class CrearContribuyenteJuridico(AjaxCreate, CreateView):
    model = Juridico
    form_class = ContribuyenteJuridicoForm
    template_name = 'contribuyente/juridico/crear.html'
    success_url = reverse_lazy('contribuyente:lista_contribuyente_juridico')
