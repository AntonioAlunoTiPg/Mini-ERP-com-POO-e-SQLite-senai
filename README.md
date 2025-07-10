# Mini-ERP-com-POO-e-SQLite-senai
# 📦 Sistema ERP Simples em Python

Este projeto é um Sistema ERP (Enterprise Resource Planning) simples desenvolvido em Python. Ele foi criado com foco em modularidade, utilizando **classes** para modelar as entidades e **SQLite** para a persistência dos dados. É um excelente ponto de partida para quem está aprendendo sobre **Programação Orientada a Objetos (POO)**, gerenciamento de banco de dados e organização de projetos em Python.

---

## 🚀 Funcionalidades Principais

O sistema oferece os seguintes módulos e funcionalidades:

### 1. Módulo de Usuários (Login e Cadastro)

- **Cadastro de Usuário**: Permite registrar novos usuários no sistema, solicitando nome, e-mail e senha. A restrição de e-mail único é imposta pelo banco de dados.
- **Autenticação de Login**: Valida as credenciais do usuário (e-mail e senha) para conceder acesso ao sistema.
- **Segurança da Senha**: As senhas são armazenadas de forma segura no banco de dados, utilizando criptografia SHA256.
- **Privacidade na Digitação**: A entrada da senha no terminal é oculta, mostrando `*****`.

### 2. Módulo CRM (Customer Relationship Management)

- **Cadastro de Clientes**: Permite registrar informações como nome, telefone e e-mail.
- **Listagem de Clientes**: Exibe uma lista completa dos clientes cadastrados.
- **Busca de Clientes**: Pesquisa por parte do nome para encontrar clientes rapidamente.

### 3. Módulo Financeiro

- **Controle de Receitas e Despesas**: Adicione lançamentos classificados como receita ou despesa.
- **Listagem de Lançamentos**: Visualize um histórico detalhado.
- **Cálculo de Saldo**: Calcula o saldo total com base nas receitas e despesas.

---

## 📁 Estrutura do Projeto

```text
erp/
├── main.py            # Ponto de entrada da aplicação
├── database.py        # Operações com SQLite
├── usuario.py         # Classe Usuario: cadastro e login
├── crm.py             # Classe Cliente: gerenciamento de clientes
├── financeiro.py      # Classe Lancamento: gestão financeira
└── utils.py           # Funções auxiliares (validação, formatação, etc.)
