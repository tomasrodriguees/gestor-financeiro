import sqlite3
from pathlib import Path

DB_PATH = Path("data/finance.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT,
            date TEXT NOT NULL,
            notes TEXT
        );
    """)
    conn.commit()
    conn.close()

def insert_transaction(type_, amount, category, date, notes):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO transactions (type, amount, category, date, notes)
        VALUES (?, ?, ?, ?, ?)
    """, (type_, amount, category, date, notes))
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