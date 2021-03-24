from django.http import JsonResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.generic import FormView, TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login, logout, update_session_auth_hash
from .forms import LoginForm, UserForm, AccountForm, GrupoForm
from apps.utils.ajax import *
from .models import User, Grupo, Permisos
from apps.administrador.models import Logs
from .mixins import PermissionRequiredMixinUser, AdminMixin


# General views
class Login(FormView):
    template_name = 'usuario/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('index')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        remember_me = form.cleaned_data['remember_me']
        if not remember_me:
            self.request.session.set_expiry(0)
            self.request.session.modified = True
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')


class RecoveryPassword(TemplateView):
    template_name = 'usuario/recovery_password.html'


class Account(LoginRequiredMixin, UpdateView):
    model = User
    form_class = AccountForm
    template_name = 'usuario/account_user.html'
    success_url = reverse_lazy('index')


class ChangePassword(LoginRequiredMixin, FormView):
    template_name = 'usuario/change_password.html'
    form_class = PasswordChangeForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'La contraseña ha sido actualizada', extra_tags='success')
            return redirect('usuario:change_password')
        return render(request, self.template_name, {'form': form})

    def get(self, request, *args, **kwargs):
        form = self.form_class(request.user)
        return render(request, self.template_name, {'form': form})


# Admin views
class ListaUsuarios(AdminMixin, AjaxList, ListView):
    model = User
    template_name = 'usuario/admin/lista_usuarios.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, *kwargs)


class CrearUsuario(AdminMixin, CreateView):
    model = User
    form_class = UserForm
    template_name = 'usuario/admin/crear_usuario.html'

    # success_url = reverse_lazy('usuario:lista_usuarios')

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST)
            if form.is_valid():
                new_user = User(
                    email=form.cleaned_data.get('email'),
                    username=form.cleaned_data.get('username'),
                    first_name=form.cleaned_data.get('first_name'),
                    last_name=form.cleaned_data.get('last_name'),
                    is_superuser=form.cleaned_data.get('is_superuser'),
                    is_active=form.cleaned_data.get('is_active'),
                    is_staff=form.cleaned_data.get('is_staff'),
                )
                new_user.set_password(form.cleaned_data.get('password1'))
                new_user.save()

                user = User.objects.last()

                for perm in form.cleaned_data.get('user_permissions'):
                    user.user_permissions.add(perm.id)
                for group in form.cleaned_data.get('groups'):
                    user.groups.add(group.id)
                message = f'{self.model.__name__} registrado correctamente'
                error = 'No hay error'
                response = JsonResponse({'message': message, 'error': error})
                response.status_code = 201
                return response
            else:
                message = f'{self.model.__name__} no se ha podido registrar'
                error = form.errors
                response = JsonResponse({'message': message, 'error': error})
                response.status_code = 404
                return response
        else:
            return redirect('usuario:lista_usuarios')


class EditarUsuario(AdminMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'usuario/admin/editar_usuario.html'
    success_url = reverse_lazy('usuario:lista_usuarios')

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST, instance=self.get_object())
            user = self.get_object()

            if form.is_valid():
                user.email = form.cleaned_data.get('email')
                user.username = form.cleaned_data.get('username')
                user.first_name = form.cleaned_data.get('first_name')
                user.last_name = form.cleaned_data.get('last_name')
                user.is_superuser = form.cleaned_data.get('is_superuser')
                user.is_active = form.cleaned_data.get('is_active')
                user.is_staff = form.cleaned_data.get('is_staff')

                row_password = form.cleaned_data.get('password1')
                if row_password != user.password:
                    user.set_password(row_password)
                permisos = form.cleaned_data.get('user_permissions')
                grupos = form.cleaned_data.get('groups')
                user.user_permissions.set(permisos)
                user.groups.set(grupos)
                user.save()

                message = f'{self.model.__name__} actualizado correctamente'
                error = 'No hay error'
                response = JsonResponse({'message': message, 'error': error})
                response.status_code = 201
                return response
            else:
                message = f'{self.model.__name__} no se ha podido actualizar'
                error = form.errors
                response = JsonResponse({'message': message, 'error': error})
                response.status_code = 404
                return response
        else:
            return redirect('usuario:lista_usuarios')


class EliminarUsuario(AdminMixin, AjaxDelete, DeleteView):
    model = User
    template_name = 'usuario/admin/eliminar.html'
    success_url = reverse_lazy('usuario:lista_usuarios')
    estado = User.is_active


# Logs Module
class ListaLogs(AdminMixin, AjaxList, ListView):
    model = Logs
    template_name = 'usuario/admin/lista_logs.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, *kwargs)


# Group module
class ListaGrupo(AdminMixin, AjaxList, ListView):
    model = Grupo
    template_name = 'usuario/grupos/lista_grupo.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, *kwargs)


class CrearGrupo(AdminMixin, AjaxCreate, CreateView):
    model = Grupo
    form_class = GrupoForm
    template_name = 'usuario/grupos/crear_grupo.html'
    success_url = reverse_lazy('usuario:lista_grupo')


class EditarGrupo(AdminMixin, AjaxUpdate, UpdateView):
    model = Grupo
    form_class = GrupoForm
    template_name = 'usuario/grupos/editar_grupo.html'
    success_url = reverse_lazy('usuario:lista_grupo')


class ListaPermisos(AdminMixin, AjaxList, ListView):
    model = Permisos
    template_name = 'usuario/permisos/lista_permisos.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, *kwargs)
