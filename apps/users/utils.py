import re
from django.core.exceptions import ValidationError

def validate_username(username):
    # Define a expressão regular para permitir letras minúsculas, números e underscores
    pattern = r'^[a-z0-9_]+$'
    
    # Verifica se o username atende à restrição de caracteres
    if not re.match(pattern, username):
        raise ValidationError('O username deve conter apenas letras minúsculas, números e underscores!')