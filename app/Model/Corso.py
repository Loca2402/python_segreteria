from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Corso(Base):
    __tablename__ = 'Corsi'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    codice = Column(Integer, unique=True)
    nome = Column(String, nullable=False)
    anno_accademico = Column(String, nullable=False)
    tipo_titolo = Column(String, nullable=False)


    id_dipartimento = Column(Integer, ForeignKey('Dipartimenti.id'), nullable=False)
    dipartimento = relationship("Dipartimento", back_populates="corsi")

    studenti = relationship("Studente", back_populates="corso")