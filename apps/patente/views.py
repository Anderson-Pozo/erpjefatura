from django.contrib import messages
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, TemplateView, CreateView
from django.http import HttpResponse, JsonResponse
from .models import Patente, DetallePatente
from apps.contribuyente.models import Natural, Juridico, Contribuyente
from apps.establecimiento.models import Establecimiento
from .forms import PatenteForm
from apps.contribuyente.forms import ContribuyenteNaturalForm as NaturalForm, ContribuyenteJuridicoForm as JuridicoForm
from apps.establecimiento.forms import EstablecimientoForm


class ListaCatastro(ListView):
    model = Patente
    template_name = 'patente/catastro/index.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, *kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Patente.objects.all():
                    data.append(i.to_json())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)


class CrearContribuyente(TemplateView):
    template_name = 'patente/apertura/paso1_contribuyente.html'

    def get(self, request, *args, **kwargs):
        form_natural = NaturalForm(self.request.GET or None, prefix="natural")
        form_juridico = JuridicoForm(self.request.GET or None, prefix="juridico")
        context = super(CrearContribuyente, self).get_context_data(**kwargs)
        context['form_natural'] = form_natural
        context['form_juridico'] = form_juridico
        return self.render_to_response(context)

    # def post(self, request, *args, **kwargs):
    #
    #     form_natural = NaturalForm(request.POST, prefix="form_natural")
    #     if form_natural.is_valid():
    #         print(form_natural)
    #         form_natural.save()
    #         messages.success(request, 'Registro creado')
    #         return redirect('patente:crear_contribuyente')
    #     else:
    #         return None

        # context = self.get_context_data(**kwargs)
        #
        # if context['form_natural'].is_valid():
        #     instance = NaturalForm.save(request.POST)
        #     messages.success(request, 'Your offer bid #{0} has been submitted.'.format(instance.pk))
        # elif context['form_juridico'].is_valid():
        #     instance = context['form_juridico'].save()
        #     messages.success(request, 'Your offer attachment #{0} has been submitted.'.format(instance.pk))
        #     # advise of any errors
        # else:
        #     messages.error('Error(s) encountered during form processing, please review below and re-submit')
        # return self.render_to_response(context)
    # success_url = reverse_lazy('patente:crear_establecimiento')


class CrearNatural(CreateView):
    model = Natural
    form_class = NaturalForm
    template_name = 'patente/apertura/paso1_contribuyente_natural.html'
    success_url = reverse_lazy('patente:crear_establecimiento')


class CrearJuridico(CreateView):
    model = Juridico
    form_class = JuridicoForm
    template_name = 'patente/apertura/paso1_contribuyente_juridico.html'
    success_url = reverse_lazy('patente:crear_establecimiento')


class CrearEstablecimiento(CreateView):
    model = Establecimiento
    form_class = EstablecimientoForm
    template_name = 'patente/apertura/paso2_establecimiento.html'
    success_url = reverse_lazy('patente:crear_patente')


class CrearPatente(CreateView):
    model = Patente
    form_class = PatenteForm
    template_name = 'patente/apertura/paso3_detalle.html'
    # success_url = reverse_lazy('patente:crear_contribuyente_natural')
