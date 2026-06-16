from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.main import Base


class Dipartimento(Base):
    __tablename__ = 'Dipartimenti'

    id = Column(Integer, primary_key=True)
    codice = Column(String, unique=True)
    nome = Column(String, unique=True)

    id_ateneo = Column(Integer, ForeignKey('Atenei.id'), nullable=False)
    ateneo = relationship("Ateneo", back_populates="dipartimento")

    corsi = relationship("Corso", back_populates="dipartimento")
