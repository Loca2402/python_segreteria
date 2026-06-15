from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()
class Corso(Base):
    __tablename__ = 'Corso'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    codice = Column(Integer, unique=True)
    nome = Column(String, nullable=False)
    anno_accademico = Column(String, nullable=False)
    tipo_titolo = Column(String, nullable=False)

    id_ateneo = Column(Integer, ForeignKey('Ateneo.id'), nullable=False)
    ateneo = relationship("Ateneo", back_populates="dipartimenti")

    corsi = relationship("Cors0", back_populates="dipartimento")