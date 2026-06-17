# app/schemas.py

from pydantic import BaseModel


class AteneoCreate(BaseModel):
    nome: str
    codice: str
    citta: str


class AteneoResponse(BaseModel):
    id: int
    nome: str
    codice: str
    citta: str

    class Config:
        from_attributes = True