from django.http import HttpResponse
from django.db.models import Exists
from django.shortcuts import render, redirect, get_object_or_404
from .utils import senha_e_valida, email_html
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.messages import constants
import os
from django.conf import settings
from .models import Ativacao
from hashlib import sha256

def cadastrar(request):
    
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, "cadastrar.html")
    
    elif request.method == "POST":
        usuario = request.POST.get("usuario")
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        confirmar_senha = request.POST.get("confirmar_senha")
        
    if not senha_e_valida(request, senha, confirmar_senha): 
        return redirect("/auth/cadastro")
    
    if User.objects.filter(Exists(User.objects.filter(username=usuario))):
            messages.add_message(request, constants.ERROR, "Usuário não disponível ou já cadastrado.")
            return redirect("/auth/cadastro/")
    
    try:
            
        user = User.objects.create_user(username = usuario,
                                        password = senha,
                                        is_active = False)
        user.save()
        
        token = sha256(f"{usuario}{email}".encode()).hexdigest()
        ativacao = Ativacao(token=token, user=user)
        ativacao.save()
        
        path_template = os.path.join(settings.BASE_DIR, "autenticacao/templates/emails/cadastro_confirmado.html")
        email_html(path_template, "Cadastro confirmado!", [email], username=usuario, link_ativacao=f"127.0.0.1:8000/auth/ativar_conta/{token}")
        
        messages.add_message(request, constants.SUCCESS, "Usuário cadastrado com sucesso.")
        return redirect("/auth/login/")
        
    except:
        messages.add_message(request, constants.ERROR, "Erro inesperado no server.")
        return redirect("/auth/cadastro/")

def logar(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/pacientes/')
        return render(request, "logar.html")
    
    elif request.method == "POST":
        usuario = request.POST.get("usuario")
        senha = request.POST.get("senha")
        
        user = auth.authenticate(username=usuario, password=senha)
        
        if not user:
            messages.add_message(request, constants.ERROR, "Usuário ou senha inválidos.")
            return redirect("/auth/login/")
        
        else:
            auth.login(request, user)
            return redirect('/pacientes/')
        
def sair(request):
    auth.logout(request)
    return redirect("/auth/login")

def ativar_conta(request, token):
    
    token = get_object_or_404(Ativacao, token=token)
    
    if token.ativo:
        messages.add_message(request, constants.WARNING, "Esse token já está ativo!")
        return redirect("/auth/login")
    
    user = User.objects.get(username=token.user.username)
    user.is_active = True
    user.save()
    token.ativo = True
    token.save()
    messages.add_message(request, constants.SUCCESS, "Conta ativada com sucesso!")
    
    return redirect("/auth/login")

