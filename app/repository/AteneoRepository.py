from sqlalchemy.orm import Session

from app.model import Ateneo


class AteneoRepository:
    @staticmethod
    def  get_all(db: Session):
        return db.query(Ateneo).all()

    @staticmethod
    def get_by_id(db: Session, ateneo_id: int):
        return db.query(Ateneo).filter(Ateneo.id == ateneo_id).first()

    @staticmethod
    def save(db:Session, ateneo_db:Ateneo):
        db.add(ateneo_db)
        db.commit()
        db.refresh(ateneo_db)
        return ateneo_db