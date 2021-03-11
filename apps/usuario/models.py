from datetime import datetime, date
from django.db import models
from django.forms import model_to_dict
from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission
from django.contrib.admin.models import LogEntry
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
    username = models.CharField('Nombre usuario', max_length=13, unique=True,
                                help_text='Debe colocar su número de RUC o su cédula')
    email = models.EmailField('Correo electrónico', max_length=60, unique=True, null=True)
    first_name = models.CharField('Nombres', max_length=100, blank=True, null=True)
    last_name = models.CharField('Apellidos', max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

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
        # item['permissions'] = {x: x for x in self.permissions.name}
        return item


class Permisos(Permission):
    class Meta:
        proxy = True

    def to_json(self):
        item = model_to_dict(self)
        item['content_type'] = self.content_type.name
        return item


class Logs(LogEntry):
    class Meta:
        proxy = True

    def get_action_color(self):
        if self.action_flag == 1:
            return 'timeline-item-marker-indicator bg-green'
        elif self.action_flag == 2:
            return 'timeline-item-marker-indicator bg-yellow'
        else:
            return 'timeline-item-marker-indicator bg-red'

    def get_action_text(self):
        if self.action_flag == 1:
            return 'creado'
        elif self.action_flag == 2:
            return 'modificado'
        else:
            return 'eliminado'

    def get_days(self):
        current_date = date.today()
        past_date = self.action_time.date()
        days = (current_date - past_date).days
        if days == 0 or -1:
            return 'Hoy'
        elif days == 1:
            return '{} día'.format(days)
        else:
            return '{} días'.format(days)
        # return days

    def to_json(self):
        item = model_to_dict(self)
        item['user'] = self.user.__str__()
        item['date'] = current_date_format(self.action_time)
        return item
