from django.contrib import admin
from .models import Parroquia, Barrio, Direccion

# Register your models here.
admin.site.register(Parroquia)
admin.site.register(Barrio)
admin.site.register(Direccion)
