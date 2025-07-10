# erp/crm.py
from database import execute_query, fetch_data, fetch_one
from utils import validar_email

class Cliente:
    def __init__(self, nome, telefone, email, id=None):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def cadastrar_cliente(self):
        """Cadastra um novo cliente no banco de dados."""
        if not validar_email(self.email):
            print("Erro: E-mail inválido.")
            return False

        query = "INSERT INTO clientes (nome, telefone, email) VALUES (?, ?, ?)"
        params = (self.nome, self.telefone, self.email)
        if execute_query(query, params):
            print(f"Cliente '{self.nome}' cadastrado com sucesso!")
            return True
        else:
            print(f"Erro ao cadastrar o cliente '{self.nome}'. Talvez o e-mail já exista.")
            return False

    @staticmethod
    def listar_clientes():
        """Lista todos os clientes cadastrados."""
        query = "SELECT * FROM clientes"
        clientes_data = fetch_data(query)
        if not clientes_data:
            print("Nenhum cliente cadastrado.")
            return []
        
        print("\n--- Clientes Cadastrados ---")
        for cliente in clientes_data:
            print(f"ID: {cliente[0]}, Nome: {cliente[1]}, Telefone: {cliente[2]}, Email: {cliente[3]}")
        print("----------------------------")
        return [Cliente(c[1], c[2], c[3], c[0]) for c in clientes_data]

    @staticmethod
    def buscar_cliente_por_nome(nome):
        """Busca um cliente pelo nome."""
        query = "SELECT * FROM clientes WHERE nome LIKE ?"
        params = (f"%{nome}%",)
        clientes_data = fetch_data(query, params)
        if not clientes_data:
            print(f"Nenhum cliente encontrado com o nome '{nome}'.")
            return []
        
        print(f"\n--- Clientes Encontrados com '{nome}' ---")
        for cliente in clientes_data:
            print(f"ID: {cliente[0]}, Nome: {cliente[1]}, Telefone: {cliente[2]}, Email: {cliente[3]}")
        print("------------------------------------------")
        return [Cliente(c[1], c[2], c[3], c[0]) for c in clientes_data]