from pydantic import BaseModel


class AteneoDTO(BaseModel):
    ateneoId: int
    nome: str
    codice: str
    citta: str

    model_config = {
        "from_attributes": True
    }