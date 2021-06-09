from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class LoginSuperUserMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return super().dispatch(request, *args, **kwargs)
        return redirect('index')


class AdminMixin(LoginRequiredMixin, object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser is False:
                messages.error(request, 'No tiene permiso para acceder a esta vista')
                return redirect('consulta:index_consulta')
        return super().dispatch(request, *args, **kwargs)


class StaffMixin(LoginRequiredMixin, object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff:
                messages.error(request, 'No tiene permiso para acceder a esta vista')
                return redirect('index')
        return super().dispatch(request, *args, **kwargs)


class PermissionRequiredMixinUser(object):
    """
        This class validate if user has all permission in views
    """
    permission_required = ('usuario.view_user', 'usuario.add_user',)
    url_redirect = None

    def get_perms(self):
        """
        This method obtain permission required define in views
        :return:  One string or tuple of permissions
        """
        if isinstance(self.permission_required, str):
            return (self.permission_required,)
        else:
            return self.permission_required

    def get_url_redirect(self):
        """
        This method verify if url_redirect is define in views
        :return: reverse_lazy('login') or url_redirect for default in view
        """
        if self.url_redirect is None:
            return reverse_lazy('login')
        return self.url_redirect

    def dispatch(self, request, *args, **kwargs):
        """
        This method make a dispatch depend if user has all permission or no
        :return: The same request if user has all required permissions
        :return: redirect value of method get_url_redirect
        """
        if request.user.has_perms(self.get_perms()):
            return super().dispatch(request, *args, **kwargs)
        messages.error(request, 'No tiene permiso para acceder a esta vista')
        return redirect(self.get_url_redirect())
