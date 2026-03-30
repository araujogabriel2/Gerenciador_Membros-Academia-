from pydantic import BaseModel, Field

class Socio(BaseModel):
    nome: str = Field(..., min_length=3, description="Nome do membro")
    idade: int = Field(..., ge=16, description="Idade do membro deve ser igual ou maior que 16")
    plano: str = Field(..., description="Tipo de plano (MENSAL, ANUAL, VIP)")
    ativo: bool = Field(default=True)

