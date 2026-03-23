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
    conn.commit()
    conn.close()
    
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
    dados = cursor.fetchall()
    conn.close()

    return [dict(linha) for linha in dados]

def listar_membros_por_id(id_membro):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM socios WHERE id = ?"(id_membro,))
    dado = cursor.fetchone()
    conn.close()

    return dict(dado) if dado else None

def atualizar_plano(socios, novo_plano, id_membro):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("UPDATE socios set plano = ? WHERE id = ? ", (novo_plano, id_membro))
    if cursor.rowcount == 0:
        conn.close()
        return {"erro": "Membro não encontrado!"}
    conn.commit()
    conn.close()

    return {
        "mensagem": f"Plano de {socios.nome} atualizado com sucesso!"
    }