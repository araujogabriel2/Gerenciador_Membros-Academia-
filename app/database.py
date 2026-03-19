import sqlite3

def conectar():
    conn = sqlite3.connect("socios.db")
    conn.row_factory = sqlite3.Row
    return conn

