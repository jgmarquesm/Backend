from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path("cadastro/", views.cadastrar, name = "cadastrar"),
    path("login/", views.logar, name = "logar"),
    path("logout/", views.sair, name = "sair")
]
