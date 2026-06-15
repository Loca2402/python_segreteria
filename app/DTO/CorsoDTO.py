from pydantic import BaseModel


class CorsoDTO(BaseModel):
    codice: int
    nome: str
    anno_accademico: str
    tipo_titolo: str