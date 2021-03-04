from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, TemplateView
from django.http import HttpResponse, JsonResponse
from apps.patente.models import Patente, DetallePatente

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
            # user = request.user.username
            user = request.GET['username']
            # user = request.POST['user']
            action = request.POST['action']
            print(user)
            if action == 'search_data':
                data = []
                for i in Patente.objects.filter(contribuyente__ruc=user):
                    data.append(i.to_json())
                print(data)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

