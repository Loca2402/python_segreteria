from pydantic import BaseModel


class DipartimentoDTO(BaseModel):
    codice: str
    nome: str