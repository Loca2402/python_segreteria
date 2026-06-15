from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine  # Nota: ho tolto 'create_index' dall'import perché non serve qui
from sqlalchemy.orm import declarative_base, sessionmaker, Session

from Model import Base, Ateneo, Dipartimento

SQLALCHEMY_DATABASE_URL = "sqlite:///./segreteria.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine) #crea tutte le tabelle all'istante.

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()