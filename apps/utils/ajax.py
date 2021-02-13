from django.shortcuts import render, redirect
from django.http import JsonResponse


class AjaxList:
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in self.model.objects.all():
                    data.append(i.to_json())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)


class AjaxCreate:
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
                # print(form.errors)
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        return self.success_url


class AjaxUpdate:
    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST, instance=self.get_object())
            if form.is_valid():
                form.save()
                message = f'{self.model.__name__} actualizado correctamente'
                error = 'There`s no error'
                response = JsonResponse({'message': message, 'error': error})
                response.status_code = 201
                return response
            else:
                message = f'{self.model.__name__} no se pudo actualizar'
                error = form.errors
                response = JsonResponse({'message': message, 'error': error})
                response.status_code = 400
                return response
        else:
            return self.success_url


class AjaxDelete:
    def delete(self, request, *args, **kwargs):
        if request.is_ajax():
            modelo = self.get_object()
            if modelo.estado:
                modelo.estado = False
            elif modelo.is_active:
                modelo.is_active = False
            modelo.save()
            message = f'{self.model.__name__} fue eliminado'
            error = 'No hay error'
            response = JsonResponse({'message': message, 'error': error})
            response.status_code = 201
            return response
        else:
            return self.success_url
