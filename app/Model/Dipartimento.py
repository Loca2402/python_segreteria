from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()
class Dipartimento(Base):
    __tablename__ = 'Dipartimenti'

    id=Column(Integer, primary_key=True)
    codice=Column(String, unique=True)
    nome=Column(String, unique=True)