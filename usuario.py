# erp/usuario.py
from database import execute_query, fetch_one
import hashlib # Desafio Extra: Criptografia de senha

class Usuario:
    def __init__(self, nome, email, senha, id=None):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = self._hash_senha(senha) # Desafio Extra: Armazena a senha criptografada

    def _hash_senha(self, senha):
        """Criptografa a senha usando SHA256."""
        return hashlib.sha256(senha.encode()).hexdigest()

    def cadastrar(self):
        """Cadastra um novo usuário no banco de dados."""
        query = "INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)"
        params = (self.nome, self.email, self.senha)
        if execute_query(query, params):
            print(f"Usuário '{self.nome}' cadastrado com sucesso!")
            return True
        else:
            print(f"Erro ao cadastrar o usuário '{self.nome}'. Talvez o e-mail já exista.")
            return False

    @staticmethod
    def autenticar(email, senha):
        """Autentica um usuário com base no email e senha."""
        hashed_senha = hashlib.sha256(senha.encode()).hexdigest() # Criptografa a senha fornecida para comparação
        query = "SELECT * FROM usuarios WHERE email = ? AND senha = ?"
        params = (email, hashed_senha)
        usuario_data = fetch_one(query, params)
        if usuario_data:
            print(f"Usuário '{usuario_data[1]}' autenticado com sucesso!")
            return Usuario(usuario_data[1], usuario_data[2], senha, usuario_data[0]) # Retorna o objeto Usuario
        else:
            print("Email ou senha inválidos.")
            return None