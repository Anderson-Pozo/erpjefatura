from datetime import datetime, date
from django.db import models
from django.forms import model_to_dict
from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission
from apps.utils.format_date import current_date_format
from apps.auditoria.mixins import AuditMixin


class UserManager(BaseUserManager):
    def _create_user(self, email, username, first_name, last_name, password, is_staff, is_superuser):
        user = self.model(
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            is_staff=is_staff,
            is_superuser=is_superuser
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, username, first_name, last_name, password=None):
        return self._create_user(email, username, first_name, last_name, password, False, False)

    def create_superuser(self, email, username, first_name, last_name, password=None):
        return self._create_user(email, username, first_name, last_name, password, True, True)


class User(AuditMixin, AbstractUser):
    username = models.CharField('Nombre usuario', max_length=10, unique=True,
                                help_text='Debe colocar su número de RUC o su cédula')
    email = models.EmailField('Correo electrónico', max_length=25, unique=False, null=True)
    first_name = models.CharField('Nombres', max_length=30, blank=True, null=True)
    last_name = models.CharField('Apellidos', max_length=30, blank=True, null=True)
    path_avatar = models.CharField('Avatar URL', max_length=100, blank=True, null=True)
    is_active = models.BooleanField('Es activo', default=True)
    is_staff = models.BooleanField('Es empleado', default=False)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def to_json(self):
        item = model_to_dict(self, exclude=['user_permissions', 'groups',])
        return item

    class Meta:
        db_table = "usuario"

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

    def avatar_name(self):
        if self.first_name and self.last_name:
            return self.first_name[0] + self.last_name[0]
        elif self.first_name:
            return self.first_name[0]
        elif self.last_name:
            return self.last_name[0]
        else:
            return 'NoN'


class Grupo(Group):
    class Meta:
        proxy = True

    def to_json(self):
        item = model_to_dict(self, exclude=['permissions', ])
        return item


class Permisos(Permission):
    class Meta:
        proxy = True

    def to_json(self):
        item = model_to_dict(self)
        item['content_type'] = self.content_type.name
        return item