from pydantic import BaseModel


class CorsoDTO(BaseModel):
    corsoId:int
    codice: int
    nome: str
    anno_accademico: str
    tipo_titolo: str

    model_config = {
        "from_attributes": True
    }