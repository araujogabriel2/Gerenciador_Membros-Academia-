from database import conectar

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
                CREATE TABLE IF NOT EXISTS socios(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    idade INTEGER NOT NULL,
                    plano TEXT NOT NULL,
                    ativo BOOLEAN NOT NULL DEFAULT 1
                )
            """)    