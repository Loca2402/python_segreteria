from sqlalchemy.orm import Session

from app.Model import Ateneo, Corso


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
