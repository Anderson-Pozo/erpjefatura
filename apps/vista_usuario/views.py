from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, TemplateView
from django.http import HttpResponse, JsonResponse
from apps.patente.models import Patente, DetallePatente
from apps.establecimiento.models import Establecimiento

# Create your views here.


class Index(TemplateView):
    # model = VistaUsuario
    template_name = 'vista_usuario/index.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, *kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            user = request.user.username
            action = request.POST['action']
            if action == 'search_data':
                data = []
                for i in Patente.objects.filter(contribuyente__ruc=user):
                    data.append(i.to_json())
                print(data)
            elif action == 'search_establ':
                data = []
                # for i in Patente.objects.filter(contribuyente__ruc=user):
                for i in Establecimiento.objects.filter(patente__contribuyente__ruc=user):
                    data.append(i.to_json())
                print(data)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

