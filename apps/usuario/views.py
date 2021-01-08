from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.views.generic import FormView, TemplateView
from django.contrib.auth import login, logout
from .forms import LoginForm


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
        # remember_me = form.cleaned_data['remember_me']
        # if not remember_me:
        #     self.request.session.set_expiry(0)
        #     self.request.session.modified = True
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')


class RecoveryPassword(TemplateView):
    template_name = 'usuario/recovery_password.html'
