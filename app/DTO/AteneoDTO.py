from pydantic import BaseModel


class AteneoDTO(BaseModel):
    nome: str
    codice: str
    citta: str