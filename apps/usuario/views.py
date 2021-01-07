from django.shortcuts import render
from django.views.generic import ListView
from .models import Usuario


# Create your views here.
class Login(ListView):
    model = Usuario
    template_name = 'usuario/login.html'
