import re
from django.contrib import messages
from django.contrib.messages import constants
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

def dados_validados(request, **kwargs):
    peso = kwargs.get("peso")
    altura = kwargs.get("altura")
    gordura = kwargs.get("gordura")
    musculo = kwargs.get("musculo")
    hdl = kwargs.get("hdl")
    ldl = kwargs.get("ldl")
    total = kwargs.get("total")
    trig = kwargs.get("trig")
    
    if (len(peso.strip()) == 0) or (len(altura.strip()) == 0) or (len(gordura.strip()) == 0) or (len(musculo.strip()) == 0) or (len(hdl.strip()) == 0) or (len(ldl.strip()) == 0) or (len(total.strip()) == 0) or (len(trig.strip()) == 0):
        messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
        return False
    
    if not peso.isnumeric():
        messages.add_message(request, constants.ERROR, 'Digite um peso válido')
        return False
    
    if not altura.isnumeric():
        messages.add_message(request, constants.ERROR, 'Digite uma alutra válida')
        return False
    
    if not gordura.isnumeric():
        messages.add_message(request, constants.ERROR, 'Digite um percentual de gordura válido')
        return False
    
    if not musculo.isnumeric():
        messages.add_message(request, constants.ERROR, 'Digite um percentual de músculo válido')
        return False
    
    if not hdl.isnumeric():
        messages.add_message(request, constants.ERROR, 'Digite um colesterol HDL válido')
        return False
    
    if not ldl.isnumeric():
        messages.add_message(request, constants.ERROR, 'Digite um colesterol LDL válido')
        return False
    
    if not total.isnumeric():
        messages.add_message(request, constants.ERROR, 'Digite um colesterol total válido')
        return False
    
    if not trig.isnumeric():
        messages.add_message(request, constants.ERROR, 'Digite triglicerídeos válidos')
        return False
    
    return True

