# erp/database.py
import sqlite3

DATABASE_NAME = 'erp_system.db'

def connect_db():
    """Conecta ao banco de dados SQLite."""
    return sqlite3.connect(DATABASE_NAME)

def create_tables():
    """Cria as tabelas necessárias no banco de dados."""
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            telefone TEXT,
            email TEXT UNIQUE
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS lancamentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo TEXT NOT NULL, -- 'receita' ou 'despesa'
            descricao TEXT NOT NULL,
            valor REAL NOT NULL,
            data TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

def execute_query(query, params=()):
    """Executa uma query de INSERT, UPDATE ou DELETE."""
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute(query, params)
        conn.commit()
        return True
    except sqlite3.IntegrityError as e:
        print(f"Erro de integridade no banco de dados: {e}")
        return False
    except Exception as e:
        print(f"Erro ao executar a query: {e}")
        return False
    finally:
        conn.close()

def fetch_data(query, params=()):
    """Busca dados no banco de dados."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(query, params)
    data = cursor.fetchall()
    conn.close()
    return data

def fetch_one(query, params=()):
    """Busca um único registro no banco de dados."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(query, params)
    data = cursor.fetchone()
    conn.close()
    return data

# No início do seu aplicativo, chame create_tables() uma vez para garantir que as tabelas existam.
if __name__ == '__main__':
    create_tables()
    print("Tabelas verificadas/criadas com sucesso!")