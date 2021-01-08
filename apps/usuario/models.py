from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


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


# Create your models here.
class User(AbstractUser):
    username = models.CharField('Nombre usuario', max_length=10, unique=True)
    email = models.EmailField('Correo electrónico', max_length=60, unique=True)
    first_name = models.CharField('Nombres', max_length=100, blank=True, null=True)
    last_name = models.CharField('Apellidos', max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        db_table = "usuario"

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


