from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()
class Ateneo(Base):
    __tablename__ = "atenei"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, unique=True)
    codice = Column(String, unique=True)
    citta= Column(String, nullable=False)

    dipartimenti = relationship("Dipartimento", back_populates="ateneo")
