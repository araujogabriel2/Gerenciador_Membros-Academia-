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
    
def registrar_membro(socios):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO socios (nome, idade, plano, ativo) VALUES(?,?,?,?)", (
        socios.nome, socios.idade, socios.plano, socios.ativo
    ))
    conn.commit()
    novo_id = cursor.lastrowid
    conn.close()

    return {
        "mensagem": f"Membro {socios.nome} cadastrado com sucesso!",
        "ID": novo_id
    }

def listar_membros():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM socios")
    conn.close()
    dados = cursor.fetchall()
    return dados