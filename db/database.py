import sqlite3
from pathlib import Path

DB_PATH = Path("data/finance.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # Criar tabela de contas (se não existir)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contas (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            tipo TEXT NOT NULL
        )
    ''')
    
    # Criar tabela de transações (com campo Conta_ID para associar à conta)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY,
            tipo TEXT NOT NULL,
            valor REAL NOT NULL,
            categoria TEXT NOT NULL,
            data TEXT NOT NULL,
            notas TEXT,
            Conta_ID INTEGER,
            FOREIGN KEY (Conta_ID) REFERENCES contas (id)
        )
    ''')
    
    conn.commit()
    conn.close()

def insert_transaction(tipo, valor, categoria, data, notas, conta_id):
    conn = sqlite3.connect('db/database.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO transactions (tipo, valor, categoria, data, notas, Conta_ID)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (tipo, valor, categoria, data, notas, conta_id))
    conn.commit()
    conn.close()

def get_all_transactions():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions ORDER BY date DESC")
    data = cursor.fetchall()
    conn.close()
    return data


def init_contas():
    conn = sqlite3.connect('db/database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contas (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            tipo TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insert_conta(nome, tipo):
    conn = sqlite3.connect('db/database.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO contas (nome, tipo) 
        VALUES (?, ?)
    ''', (nome, tipo))
    conn.commit()
    conn.close()

def get_all_contas():
    conn = sqlite3.connect('db/database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM contas')
    contas = cursor.fetchall()
    conn.close()
    return contas

def get_saldo_conta(conta_id):
    conn = sqlite3.connect('db/database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT SUM(Valor) FROM transactions WHERE Conta_ID = ?', (conta_id,))
    saldo = cursor.fetchone()[0]
    conn.close()
    return saldo if saldo else 0.0
    