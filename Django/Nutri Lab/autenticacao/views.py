from django.http import HttpResponse
from django.shortcuts import render, redirect
from .utils import senha_e_valida
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.messages import constants

def cadastrar(request):
    
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("/")
        return render(request, "cadastrar.html")
    
    elif request.method == "POST":
        usuario = request.POST.get("usuario")
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        confirmar_senha = request.POST.get("confirmar_senha")
        
    if not senha_e_valida(request, senha, confirmar_senha): 
        return redirect("/auth/cadastro")
    
    try:
        user = User.objects.create_user(username = usuario,
                                        password = senha,
                                        is_active = False)
        user.save()
        messages.add_message(request, constants.SUCCESS, "Usuário cadastrado com sucesso.")
        return redirect("/auth/login/")
    
    except:
        messages.add_message(request, constants.ERROR, "Erro inesperado no server.")
        return redirect("/auth/cadastro/")
    
    #return HttpResponse("Até aqui está tudo okay")
        
        

def logar(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("/")
        return render(request, "logar.html")
    
    elif request.method == "POST":
        usuario = request.POST.get("usuario")
        senha = request.POST.get("senha")
        
        user = auth.authenticate(username=usuario, password=senha)
        
        if not user:
            messages.add_message(request, messages.ERROR, "Usuário ou senha inválidos.")
            return redirect("/auth/login/")
        
        else:
            return redirect("/")
        
def sair(request):
    user.logout(request)
    return redirect("/auth/login")
