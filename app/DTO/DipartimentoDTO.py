from pydantic import BaseModel


class DipartimentoDTO(BaseModel):
    dipartimentoId: int
    codice: str
    nome: str

    model_config = {
        "from_attributes": True
    }