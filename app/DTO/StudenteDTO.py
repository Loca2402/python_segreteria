from pydantic import BaseModel


class StudenteDTO(BaseModel):
    studenteId: int
    matricola: str
    nome: str
    cognome: str
    data_nascita:str

    model_config = {
        "from_attributes": True
    }