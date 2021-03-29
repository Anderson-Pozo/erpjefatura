from django.views.generic.base import View
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from .models import Direccion
from django.db.models import Q


class GetDirecciones(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs, ):
        data = {}
        try:
            action = request.POST['action']
            if action == 'get_direccion':
                data = []
                for i in Direccion.objects.filter(
                        Q(barrio__nombre__icontains=request.POST['term']) |
                        Q(calle_principal__icontains=request.POST['term']) |
                        Q(barrio__parroquia__nombre__icontains=request.POST['term']))[0:10]:
                    item = i.to_json()
                    item['text'] = i.get_select2()
                    data.append(item)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
