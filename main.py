# erp/main.py
from database import create_tables
from usuario import Usuario
from crm import Cliente
from financeiro import Lancamento
import os
import getpass # <-- Adicione esta linha

def limpar_tela():
    """Limpa o console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_principal():
    """Exibe o menu principal do sistema ERP."""
    while True:
        print("\n--- Menu Principal ---")
        print("1. Módulo CRM")
        print("2. Módulo Financeiro")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            menu_crm()
        elif opcao == '2':
            menu_financeiro()
        elif opcao == '3':
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_crm():
    """Exibe o menu do módulo CRM."""
    while True:
        print("\n--- Módulo CRM ---")
        print("1. Cadastrar Cliente")
        print("2. Buscar Cliente por Nome")
        print("3. Listar Clientes")
        print("4. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print("\n--- Cadastrar Novo Cliente ---")
            nome = input("Nome do cliente: ")
            telefone = input("Telefone do cliente: ")
            email = input("Email do cliente: ")
            cliente = Cliente(nome, telefone, email)
            cliente.cadastrar_cliente()
        elif opcao == '2':
            print("\n--- Buscar Cliente ---")
            nome_busca = input("Digite o nome ou parte do nome do cliente para buscar: ")
            Cliente.buscar_cliente_por_nome(nome_busca)
        elif opcao == '3':
            Cliente.listar_clientes()
        elif opcao == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_financeiro():
    """Exibe o menu do módulo Financeiro."""
    while True:
        print("\n--- Módulo Financeiro ---")
        print("1. Adicionar Receita")
        print("2. Adicionar Despesa")
        print("3. Listar Lançamentos")
        print("4. Mostrar Saldo Total")
        print("5. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print("\n--- Adicionar Receita ---")
            descricao = input("Descrição da receita: ")
            try:
                valor = float(input("Valor da receita: "))
                lancamento = Lancamento('receita', descricao, valor)
                lancamento.adicionar_lancamento()
            except ValueError:
                print("Valor inválido. Por favor, insira um número.")
        elif opcao == '2':
            print("\n--- Adicionar Despesa ---")
            descricao = input("Descrição da despesa: ")
            try:
                valor = float(input("Valor da despesa: "))
                lancamento = Lancamento('despesa', descricao, valor)
                lancamento.adicionar_lancamento()
            except ValueError:
                print("Valor inválido. Por favor, insira um número.")
        elif opcao == '3':
            Lancamento.listar_lancamentos()
        elif opcao == '4':
            Lancamento.saldo_total()
        elif opcao == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

def tela_login_cadastro():
    """Exibe a tela de login ou cadastro de usuário."""
    while True:
        limpar_tela()
        print("--- Bem-vindo ao ERP Simples ---")
        print("1. Fazer Login")
        print("2. Cadastrar Novo Usuário")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            email = input("Email: ")
            senha = getpass.getpass("Senha: ") # <-- Modificado aqui
            usuario_autenticado = Usuario.autenticar(email, senha)
            if usuario_autenticado:
                menu_principal()
                break 
            else:
                input("Pressione Enter para tentar novamente...") 
        elif opcao == '2':
            print("\n--- Cadastro de Novo Usuário ---")
            nome = input("Nome: ")
            email = input("Email: ")
            senha = getpass.getpass("Senha: ") # <-- Modificado aqui
            novo_usuario = Usuario(nome, email, senha)
            if novo_usuario.cadastrar():
                print("Usuário cadastrado com sucesso! Faça login para continuar.")
                input("Pressione Enter para continuar...")
            else:
                input("Pressione Enter para tentar novamente...")
        elif opcao == '3':
            print("Saindo do ERP. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")
            input("Pressione Enter para continuar...")

if __name__ == '__main__':
    create_tables()
    tela_login_cadastro()