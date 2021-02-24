from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse, JsonResponse
from apps.utils.ajax import AjaxList, AjaxCreate, AjaxUpdate, AjaxDelete
from .forms import AlcabalaForm
from .models import Alcabala,Comprador


class ListaAlcabala(AjaxList, ListView):
    model = Alcabala
    template_name = 'alcabala-plusvalia/index-alcabala.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, *kwargs)


class CrearAlcabala(CreateView):
    model = Alcabala
    form_class = AlcabalaForm
    template_name = 'alcabala-plusvalia/registro/paso1_alcabala.html'
    success_url = reverse_lazy('alcabala:lista_alcabala')

    # def post(self, request, *args, **kwargs):
    #     data = {}
    #     try:
    #         action = request.POST['action']
            # if action == 'search_product_id':
            #     data = [{'id': '', 'text': '------------'}]
            #     for i in Alcabala.objects.filter(id=request.POST['id']):
            #         data.append({'id': i.id, 'text': i.comprador, 'data': i.cat.toJSON()})
        #     if action == 'autocomplete':
        #         data = []
        #         for i in Comprador.objects.filter(nombres__icontains=request.POST['term'])[0:5]:
        #             item = i.toJSON()
        #             item['text'] = i.nombres
        #             data.append((item))
        #             print(data)
        #     else:
        #         data['error'] = 'ha ocurrido un error'
        # except Exception as e:
        #     data['error'] = str(e)
        # return JsonResponse(data, safe=False)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            # if action == 'search_product_id':
            #     data = [{'id': '', 'text': '------------'}]
            #     for i in Comprador.objects.filter(cat_id=request.POST['id']):
            #         data.append({'id': i.id, 'text': i.name, 'data': i.cat.toJSON()})
            if action == 'autocomplete':
                data = []
                for i in Comprador.objects.filter(nombres__icontains=request.POST['term'])[0:5]:
                    item = i.toJSON()
                    item['value'] = i.nombres
                    data.append(item)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)