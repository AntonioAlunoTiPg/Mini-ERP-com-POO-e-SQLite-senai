# erp/utils.py
import re
from datetime import datetime

def validar_email(email):
    """Valida o formato de um endereço de e-mail."""
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

def formatar_data_atual():
    """Retorna a data atual no formato YYYY-MM-DD."""
    return datetime.now().strftime('%Y-%m-%d')