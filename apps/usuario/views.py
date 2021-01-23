from django.http import JsonResponse
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.generic import FormView, TemplateView, ListView
from django.contrib.auth import login, logout
from .forms import LoginForm
from .models import User
from apps.utils.ajax import AjaxCreate


# Create your views here.
class Login(FormView):
    template_name = 'usuario/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('index')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        remember_me = form.cleaned_data['remember_me']
        if not remember_me:
            self.request.session.set_expiry(0)
            self.request.session.modified = True
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)


class ListaUsuarios(ListView):
    model = User
    template_name = 'usuario/admin/lista_usuarios.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, *kwargs)

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


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')


class RecoveryPassword(TemplateView):
    template_name = 'usuario/recovery_password.html'


class Account(TemplateView):
    template_name = 'usuario/account_user.html'


class ChangePassword(TemplateView):
    template_name = 'usuario/change_password.html'