from sqlalchemy.orm import Session

from app.Model import Dipartimento


class DipartimentoRepository():
    @staticmethod
    def get_all(db:Session):
        return db.query(Dipartimento).all()

    @staticmethod
    def save(db: Session, dipartimento_db: Dipartimento):
        db.add(dipartimento_db)
        db.commit()
        db.refresh(dipartimento_db)
        return dipartimento_db

    @staticmethod
    def get_by_ateneo(db: Session, ateneo_id:int):
        return db.query(Dipartimento).filter(Dipartimento.id == ateneo_id).first()
