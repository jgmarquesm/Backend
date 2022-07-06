import re
from django.contrib import messages
from django.contrib.messages import constants

def senha_e_valida(request, senha, confirmar_senha):
    
    if len(senha) < 8:
        messages.add_message(request, constants.ERROR, "Sua senha deve conter no mínimo 8 caracteres.")
        return False
    
    if not (senha == confirmar_senha):
        messages.add_message(request, constants.ERROR, "As senhas não coincidem!")
        return False
    
    if not re.search("[A-Z]", senha):
        messages.add_message(request, constants.ERROR, "A senha deve conter ao menos um caracter maiúsculo.")
        return False
    
    if not re.search("[a-z]", senha):
        messages.add_message(request, constants.ERROR, "A senha deve conter ao menos um caracter minúsculo.")
        return False
    
    if not re.search("[0-9]", senha):
        messages.add_message(request, constants.ERROR, "A senha deve conter ao menos um número.")
        return False
    
    '''if not re.search("[!@#$%&*()/\|-+=_^~`]", senha):
        messages.add_message(request, constants.ERROR, "A senha deve conter pelo menos um caracter.")
        return False'''
    
    return True