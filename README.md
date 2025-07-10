```
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

erp/
├── main.py            # Ponto de entrada da aplicação
├── database.py        # Operações com SQLite
├── usuario.py         # Classe Usuario: cadastro e login
├── crm.py             # Classe Cliente: gerenciamento de clientes
├── financeiro.py      # Classe Lancamento: gestão financeira
└── utils.py           # Funções auxiliares (validação, formatação, etc.)

---

## 🛠️ Como Usar

### Pré-requisitos

Python 3 instalado

Nenhuma biblioteca externa é necessária. Usa apenas:

- sqlite3
- hashlib
- datetime
- re
- os
- getpass

### Instalação

Clone o repositório:

git clone [URL_DO_SEU_REPOSITORIO]
cd erp

Ou baixe o ZIP, extraia e navegue até a pasta erp/.

### Execução

Execute o sistema com:

python main.py

Siga as instruções exibidas no terminal para login ou cadastro.

---

## 💡 Pontos de Aprendizado e Dicas

- POO na Prática: Classes bem definidas representam entidades do sistema.
- Design Modular: Separação de responsabilidades facilita manutenção e leitura.
- Interação com Banco de Dados: CRUD básico com sqlite3.
- Tratamento de Exceções: Uso de try-except para lidar com erros comuns.
- Segurança Básica: Hash de senhas usando SHA256.

---

## ✨ Próximos Passos e Desafios (Para Alunos Avançados)

- ✅ Edição e Exclusão: Adicionar UPDATE e DELETE para Cliente, Usuário e Lançamentos.
- ✅ Validações Robustas: Formato de telefone, campos obrigatórios, etc.
- ✅ Interface Gráfica (GUI): Usar Tkinter, PyQt, Kivy ou outra biblioteca.
- ✅ Relatórios Avançados: Filtros por data, tipo, categorias, exportação.

---

Este projeto é ideal para quem está aprendendo sobre organização de software, lógica de programação e conceitos básicos de sistemas ERP.
```
