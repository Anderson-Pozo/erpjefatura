from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, TemplateView, CreateView
from django.http import HttpResponse, JsonResponse
from .models import Establecimiento
from apps.utils.ajax import AjaxCreate
from .forms import EstablecimientoForm



# Create your views here.
class ListaEstablecimiento(ListView):
    model = Establecimiento
    template_name = 'establecimiento/index.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, *kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Establecimiento.objects.all():
                    data.append(i.to_json())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)


class CrearEstablecimiento(AjaxCreate, CreateView):
    model = Establecimiento
    template_name = 'establecimiento/crear_establecimiento.html'
    form_class = EstablecimientoForm
    success_url = reverse_lazy('establecimeinto:lista_establecimiento')

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
    #     return redirect('establecimiento:lista_establecimiento')