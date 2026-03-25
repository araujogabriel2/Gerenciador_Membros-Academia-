from fastapi import APIRouter, HTTPException
from app import crud, models

router = APIRouter()

@router.post("/socios", status_code=201)
def cadastrar_socio(socio:models.Socio):
    sucesso = crud.registrar_membro(socio)

    if not sucesso:

        raise HTTPException(
            status_code=500, 
            detail="Não foi possível cadastrar sócio."
        )
    
    return {
        "message": f'{socio.nome} cadastrado com sucesso!'
    }

@router.get("/socios")
def listar_socios():
    socios = crud.listar_membros()
    
    if socios is None:
        raise HTTPException(
            status_code=500, 
            detail="Não foi possível listar sócios."
        )
    
    return socios

@router.get("/socios/{id_membro}")
def buscar_id(id_membro:int):
    membro = crud.listar_membros_por_id(id_membro)

    if membro is False:
        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado."

        )

    if membro is None:
        raise HTTPException(
            status_code=500,
            detail="Erro ao buscar membro."
        )
    
    return membro

@router.put("/socios/{id_membro}")
def atualizar_plano(novo_plano:str, id_membro:int):
    membro_atualizado = crud.atualizar_plano(novo_plano, id_membro)

    if membro_atualizado is False:
        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado!"
        )
    
    if membro_atualizado is None:
        raise HTTPException(
            status_code=500,
            detail="Não foi possível atualizar o plano."
        )
    return {"message": "Membro atualizado com sucesso!"}

@router.delete("/socios/{id_membro}")
def deletar_membro(id_membro:int):
    resultado = crud.deletar_membro(id_membro)

    if resultado is False:
        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado!"
        )
    if resultado is None:
        raise HTTPException(
            status_code=500,
            detail="Não foi possível deletar membro!"
        )
    return {"message": "Membro deletado com sucesso!"}