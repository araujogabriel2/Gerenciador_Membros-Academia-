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
    
