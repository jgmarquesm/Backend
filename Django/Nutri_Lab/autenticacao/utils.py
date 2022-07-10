import re
from django.contrib import messages
from django.contrib.messages import constants
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

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

def email_html(path_template, assunto, para, **kwargs):
    
    html_content = render_to_string(path_template, kwargs)
    text_content = strip_tags(html_content)
    
    email = EmailMultiAlternatives(assunto, text_content, settings.EMAIL_HOST_USER, para)
    
    email.attach_alternative(html_content, "text/html")
    email.send()
    return {'status': 1}

