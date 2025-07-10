# erp/financeiro.py
from database import execute_query, fetch_data, fetch_one # Corrected: Import from your database.py
from utils import formatar_data_atual                 # Corrected: Import from your utils.py

class Lancamento:
    def __init__(self, tipo, descricao, valor, data=None, id=None):
        self.id = id
        self.tipo = tipo # 'receita' ou 'despesa'
        self.descricao = descricao
        self.valor = float(valor)
        self.data = data if data else formatar_data_atual()

    def adicionar_lancamento(self):
        """Adiciona uma nova receita ou despesa no banco de dados."""
        if self.tipo not in ['receita', 'despesa']:
            print("Erro: Tipo de lançamento inválido. Use 'receita' ou 'despesa'.")
            return False
        if self.valor <= 0:
            print("Erro: O valor do lançamento deve ser positivo.")
            return False

        query = "INSERT INTO lancamentos (tipo, descricao, valor, data) VALUES (?, ?, ?, ?)"
        params = (self.tipo, self.descricao, self.valor, self.data)
        if execute_query(query, params):
            print(f"Lançamento ({self.tipo}) de '{self.descricao}' no valor de R$ {self.valor:.2f} adicionado com sucesso!")
            return True
        else:
            print("Erro ao adicionar o lançamento.")
            return False

    @staticmethod
    def listar_lancamentos():
        """Lista todos os lançamentos (receitas e despesas)."""
        query = "SELECT * FROM lancamentos ORDER BY data DESC"
        lancamentos_data = fetch_data(query)
        if not lancamentos_data:
            print("Nenhum lançamento registrado.")
            return []
        
        print("\n--- Lançamentos Registrados ---")
        for lancamento in lancamentos_data:
            print(f"ID: {lancamento[0]}, Tipo: {lancamento[1].capitalize()}, Descrição: {lancamento[2]}, Valor: R$ {lancamento[3]:.2f}, Data: {lancamento[4]}")
        print("-------------------------------")
        return [Lancamento(l[1], l[2], l[3], l[4], l[0]) for l in lancamentos_data]

    @staticmethod
    def saldo_total():
        """Calcula o saldo total (receitas - despesas)."""
        query_receitas = "SELECT SUM(valor) FROM lancamentos WHERE tipo = 'receita'"
        query_despesas = "SELECT SUM(valor) FROM lancamentos WHERE tipo = 'despesa'"

        total_receitas = fetch_one(query_receitas)[0] or 0
        total_despesas = fetch_one(query_despesas)[0] or 0

        saldo = total_receitas - total_despesas
        print(f"\n--- Saldo Financeiro ---")
        print(f"Receitas Totais: R$ {total_receitas:.2f}")
        print(f"Despesas Totais: R$ {total_despesas:.2f}")
        print(f"Saldo Atual: R$ {saldo:.2f}")
        print("------------------------")
        return saldo