# app/routers/atenei.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.model import Ateneo
from app.schemas import AteneoCreate, AteneoResponse

router = APIRouter(
    prefix="/api/atenei",
    tags=["Atenei"]
)


@router.get("", response_model=list[AteneoResponse])
def get_atenei(db: Session = Depends(get_db)):
    return db.query(Ateneo).all()


@router.post("", response_model=AteneoResponse)
def crea_ateneo(request: AteneoCreate, db: Session = Depends(get_db)):
    nuovo_ateneo = Ateneo(
        nome=request.nome,
        codice=request.codice,
        citta=request.citta
    )

    db.add(nuovo_ateneo)
    db.commit()
    db.refresh(nuovo_ateneo)

    return nuovo_ateneo