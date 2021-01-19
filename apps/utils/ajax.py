from django.shortcuts import render, redirect
from django.http import JsonResponse


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
