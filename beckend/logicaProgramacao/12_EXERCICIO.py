#Crie uma função que valide se a senha esta correta

import re

def validar_senha(senha):
    if len(senha) < 8:
        return "Senha muito curta. Mínimo 8 caracteres."
    
    if not re.search(r"[A-Z]", senha):
        return "Senha deve conter pelo menos uma letra maiúscula."
    
    if not re.search(r"[a-z]", senha):
        return "Senha deve conter pelo menos uma letra minúscula."
    
    if not re.search(r"\d", senha):
        return "Senha deve conter pelo menos um número."
    
    if not re.search(r"[!@#$%&*]", senha):
        return "Senha deve conter pelo menos um caractere especial (!@#$%&*)."
    
    return "Senha válida!"
