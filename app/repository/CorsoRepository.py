from sqlalchemy.orm import Session

from app.model import Ateneo, Corso


class CorsoRepository:
    @staticmethod
    def get_all(db: Session):
        return db.query(Corso).all()

    @staticmethod
    def save(db: Session, corso_db: Corso):
        corso_db.add(corso_db)
        corso_db.commit()
        corso_db.refresh(corso_db)
        return corso_db

    @staticmethod
    def get_by_id(db: Session, corso_id: int):
        return db.query(Corso).filter(Corso.id == corso_id).first()

    @staticmethod
    def cerca_corso_per_filtri(db:Session, nome:str = None, tipo_titolo: str= None, anno_accademico: str=None):
        query=db.query(Corso)
        if nome:
            query = query.filter(Corso.nome.ilike(f"%{nome}%"))
        if tipo_titolo:
            query = query.filter(Corso.tipo_titolo == tipo_titolo)
        if anno_accademico:
            query = query.filter(Corso.anno_accademico== anno_accademico)

        return query.all()