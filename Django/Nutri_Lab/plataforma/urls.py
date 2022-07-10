from unicodedata import name
from django.urls import path, include
from . import views

urlpatterns = [
    path("pacientes/", views.paciente, name="pacientes"),
    path('dados_paciente/', views.dados_paciente_listar, name="dados_paciente_listar"),
    path('dados_paciente/<str:id>/', views.dados_paciente, name="dados_paciente"),
    path('grafico_peso/<str:id>/', views.grafico_peso, name="grafico_peso"),
    path('plano_alimentar_listar/', views.plano_alimentar_listar, name="plano_alimentar_listar"),
    path('plano_alimentar/<str:id>/', views.plano_alimentar, name="plano_alimentar"),
    path('refeicao/<str:id>/', views.refeicao, name="refeicao"),
    path('opcao/<str:id>/', views.opcao, name="opcao"),
    path('download/refeicoes/<str:id>/', views.download_refeicoes, name="download")
]
