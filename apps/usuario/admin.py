from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from .models import User
from .forms import UserForm


# class UserAdmin(admin.ModelAdmin):
#     form = UserForm


admin.site.register(User)
admin.site.register(ContentType)
admin.site.register(Permission)
