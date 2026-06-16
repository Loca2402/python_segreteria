from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.main import Base

class Studente(Base):
    __tablename__ = 'Studente'
    id = Column(Integer, primary_key=True)
    matricola = Column(String, nullable=False, unique=True)
    nome = Column(String, nullable=False)
    cognome = Column(String, nullable=False)
    data_nascita = Column(String, nullable=False)
    codice_fiscale = Column(String, nullable=False)
    sesso = Column(String, nullable=False)

    id_corso = Column(Integer, ForeignKey('Corsi.id'), nullable=False)
    corso = relationship("Corso", back_populates="studenti")

    recapito = relationship("Recapito", back_populates="studente")